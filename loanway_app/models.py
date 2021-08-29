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
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    dependants = models.PositiveIntegerField()
    applicant_income = models.PositiveIntegerField()
    coapplicant_income = models.PositiveIntegerField()
    loan_amount = models.PositiveIntegerField()
    loan_term = models.PositiveIntegerField()
    credit_history = models.IntegerField()
    gender = models.CharField(max_length=15, choices=GENDER_CHOICES)
    married = models.CharField(max_length=15, choices=MARRIED_CHOICES)
    graduate_info = models.CharField(max_length=30, choices=GRADUATED_CHOICES)
    self_employed = models.CharField(max_length = 10, choices=SELFEMPLOYED_CHOICES)
    area = models.CharField(max_length=20, choices=PROPERTY_CHOICES)


    def __str__(self):
        return f"{self.first_name} {self.last_name}'s loan application"