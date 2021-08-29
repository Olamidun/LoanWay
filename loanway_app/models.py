from django.db import models

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
        ('Not_Graduate', 'Not_Graduated')
    )
    SELFEMPLOYED_CHOICES = (
        ('Yes', 'yes'),
        ('No', 'no')
    )
    PROPERTY_CHOICES = (
        ('Rural', 'Rural'),
        ('Semiurban', 'Semiurban'),
        ('urban', 'Urban')
    )
    First_name = models.CharField(max_length=50)
    Last_name = models.CharField(max_length=50)
    Email = models.EmailField()
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


    def __str__(self):
        return f"{self.First_name} {self.Last_name}'s loan application"