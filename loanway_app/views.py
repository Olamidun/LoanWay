from contextlib import closing
from django.db import models
from django.shortcuts import render
import pandas
from rest_framework import generics
import sklearn
import json
import joblib
import numpy
import pickle
from .serializers import ApprovalSerializer
from .models import Approval
from .ml_function import ohe_value
from rest_framework import status, viewsets
from django.core import serializers
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from django.http import JsonResponse, request


# Create your views here.

@api_view(["POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def approve_or_reject_loan(request):
    loan_model = joblib.load("loan_model.pkl")
    applicants_data_dict = request.data
    applicants_data_dict['ApplicantIncome']  = applicants_data_dict['ApplicantIncome'] / 500
    applicants_data_dict['CoapplicantIncome']  = applicants_data_dict['CoapplicantIncome'] / 500
    applicants_data_dict['LoanAmount']  = applicants_data_dict['LoanAmount'] / 500

    print(applicants_data_dict)
    serializers = ApprovalSerializer(data=applicants_data_dict)
    if request.method == "POST":
        if serializers.is_valid():
            serializers.save(user=request.user)
            applicants_data = pandas.DataFrame(applicants_data_dict, index=[0])
            applicants_data['LoanAmount'] = numpy.log(applicants_data['LoanAmount'])
            applicants_data['Total_Income'] = applicants_data['ApplicantIncome'] + applicants_data['CoapplicantIncome']
            applicants_data['EMI'] = applicants_data['LoanAmount'] / applicants_data['Loan_Amount_Term']
            applicants_data['Balance_Income'] = applicants_data['Total_Income'] - (applicants_data['EMI'] * 100)
            applicants_data['Total_Income_Log'] = numpy.log(applicants_data['Total_Income'])
            applicants_data = applicants_data.drop(['First_name', 'Last_name', 'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount', 'Loan_Amount_Term'], axis=1)
            
            applicants_data = ohe_value(applicants_data)

            prediction = loan_model.predict(applicants_data)
            value = pandas.DataFrame(prediction, columns=['status'])
            value = value.replace({1: True, 0: False})
            context = serializers.data
            context['eligible_for_loan'] = value.iloc[0]['status']
            if context['eligible_for_loan'] == True:
                approval = Approval.objects.get(id=context['id'])
                approval.eligible_for_loan = True
                approval.save()
            return Response(context, status=status.HTTP_201_CREATED)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(serializers.errors, status=status.HTTP_405_METHOD_NOT_ALLOWED)


class ListUserAppliedLoans(generics.ListAPIView):
    serializer_class = ApprovalSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )
    def get_queryset(self):
        approval = Approval.objects.filter(user=self.request.user)
        return approval


class RetrieveUserAppliedLoans(generics.RetrieveAPIView):
    serializer_class = ApprovalSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )
    lookup_field = "id"

    def get_queryset(self):
        approval = Approval.objects.filter(id = self.kwargs.get('id'))
        return approval