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
from rest_framework import viewsets
from django.core import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from django.http import JsonResponse


# Create your views here.

@api_view(["POST"])
def approve_or_reject_loan(request):

    loan_model = joblib.load("loan_model.pkl")
    applicants_data_dict = request.data
    serializers = ApprovalSerializer(data=applicants_data_dict)
    if serializers.is_valid():
        serializers.save()
    # applicants_data_item = list(applicants_data_dict.items())
    applicants_data = pandas.DataFrame(applicants_data_dict, index=[0])
    print(applicants_data)
    applicants_data['LoanAmount'] = numpy.log(applicants_data['LoanAmount'])
    applicants_data['Total_Income'] = applicants_data['ApplicantIncome'] + applicants_data['CoapplicantIncome']
    applicants_data['EMI'] = applicants_data['LoanAmount'] /applicants_data['Loan_Amount_Term']
    applicants_data['Balance_Income'] = applicants_data['Total_Income'] - (applicants_data['EMI'] * 100)
    applicants_data['Total_Income_Log'] = numpy.log(applicants_data['Total_Income'])
    applicants_data = applicants_data.drop(['First_name', 'Last_name', 'Email', 'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount', 'Loan_Amount_Term'], axis=1)
    applicants_data = pandas.get_dummies(applicants_data)

    prediction = loan_model.predict(applicants_data)
    value = pandas.DataFrame(prediction, columns=['status'])
    value = value.replace({1: "Your Loan has been approved, congratulations!", 0: "Sorry! We cannot approve your loan at this time"})
    return Response(value)


class CheckEligibilty(generics.CreateAPIView):
    serializer_class = ApprovalSerializer
    def perform_create(self, serializer):
        loan_model = joblib.load("loan_model.pkl")
        applicants_data_dict = self.request.data
        serializer.save()
        # applicants_data_item = list(applicants_data_dict.items())
        applicants_data = pandas.DataFrame(applicants_data_dict, index=[0])
        print(applicants_data)
        applicants_data['LoanAmount'] = numpy.log(applicants_data['LoanAmount'])
        applicants_data['Total_Income'] = applicants_data['ApplicantIncome'] + applicants_data['CoapplicantIncome']
        applicants_data['EMI'] = applicants_data['LoanAmount'] /applicants_data['Loan_Amount_Term']
        applicants_data['Balance_Income'] = applicants_data['Total_Income'] - (applicants_data['EMI'] * 100)
        applicants_data['Total_Income_Log'] = numpy.log(applicants_data['Total_Income'])
        applicants_data = applicants_data.drop(['First_name', 'Last_name', 'Email', 'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount', 'Loan_Amount_Term'], axis=1)
        applicants_data = pandas.get_dummies(applicants_data)


        prediction = loan_model.predict(applicants_data)
        