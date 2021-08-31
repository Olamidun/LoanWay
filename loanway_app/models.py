from django.db import models
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

# for user in User.objects.all():
#     Token.objects.get_or_create(user=user)

# Create your models here.

class Approval(models.Model):
    GENDER_CHOICES = (
        ('Male', 'male'),
        ('Female', 'female')
    )
    MARRIED_CHOICES = (
        ('Yes', 'Married'),
        ('No', 'Single')
    )
    GRADUATED_CHOICES = (
        ('Graduate', 'Graduated'),
        ('Not Graduate', 'Not_Graduated')
    )
    SELFEMPLOYED_CHOICES = (
        ('Yes', 'yes'),
        ('No', 'no')
    )
    PROPERTY_CHOICES = (
        ('Rural', 'Rural'),
        ('Semiurban', 'Semiurban'),
        ('Urban', 'Urban')
    )
    First_name = models.CharField(max_length=50)
    Last_name = models.CharField(max_length=50)
    Email = models.EmailField(unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    Dependents = models.PositiveIntegerField()
    ApplicantIncome = models.PositiveIntegerField()
    CoapplicantIncome = models.PositiveIntegerField()
    LoanAmount = models.FloatField()
    Loan_Amount_Term = models.PositiveIntegerField()
    Credit_History = models.IntegerField()
    Gender = models.CharField(max_length=15, choices=GENDER_CHOICES)
    Married = models.CharField(max_length=15, choices=MARRIED_CHOICES)
    Education = models.CharField(max_length=30, choices=GRADUATED_CHOICES)
    Self_Employed = models.CharField(max_length = 10, choices=SELFEMPLOYED_CHOICES)
    Property_Area = models.CharField(max_length=20, choices=PROPERTY_CHOICES)
    date_applied = models.DateTimeField(auto_now_add=True)
    eligible_for_loan = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.id}'s loan application"
