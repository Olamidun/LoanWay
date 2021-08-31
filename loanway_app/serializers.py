import pandas
import numpy
import joblib
from .models import Approval
from .ml_function import ohe_value
from rest_framework import serializers


class ApprovalSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    # def to_representation(self, instance):
        # representation = super().to_representation(instance)
        # loan_model = joblib.load("loan_model.pkl")
        # print(loan_model)
        # applicants_data_dict = self.validated_data.
        # print(applicants_data_dict)
        # # serializers = ApprovalSerializer(data=applicants_data_dict)
        # # applicants_data_item = list(applicants_data_dict.items())
        # applicants_data = pandas.DataFrame(applicants_data_dict, index=[0])
        # applicants_data['LoanAmount'] = numpy.log(applicants_data['LoanAmount'])
        # applicants_data['Total_Income'] = applicants_data['ApplicantIncome'] + applicants_data['CoapplicantIncome']
        # applicants_data['EMI'] = applicants_data['LoanAmount'] /applicants_data['Loan_Amount_Term']
        # applicants_data['Balance_Income'] = applicants_data['Total_Income'] - (applicants_data['EMI'] * 100)
        # applicants_data['Total_Income_Log'] = numpy.log(applicants_data['Total_Income'])
        # applicants_data = applicants_data.drop(['First_name', 'Last_name', 'Email', 'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount', 'Loan_Amount_Term'], axis=1)
        
        # applicants_data = ohe_value(applicants_data)

        # prediction = loan_model.predict(applicants_data)
        # value = pandas.DataFrame(prediction, columns=['status'])
        # value = value.replace({1: "Your Loan has been approved, congratulations!", 0: "Sorry! We cannot approve your loan at this time"})
        # representation['eligibility_status'] = value
        # return representation

    class Meta:
        model = Approval
        fields = '__all__'
        