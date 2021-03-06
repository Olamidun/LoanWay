# Generated by Django 3.2.6 on 2021-08-29 08:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loanway_app', '0005_approval_date_applied'),
    ]

    operations = [
        migrations.RenameField(
            model_name='approval',
            old_name='applicant_income',
            new_name='ApplicantIncome',
        ),
        migrations.RenameField(
            model_name='approval',
            old_name='coapplicant_income',
            new_name='CoapplicantIncome',
        ),
        migrations.RenameField(
            model_name='approval',
            old_name='credit_history',
            new_name='Credit_History',
        ),
        migrations.RenameField(
            model_name='approval',
            old_name='dependants',
            new_name='Dependants',
        ),
        migrations.RenameField(
            model_name='approval',
            old_name='graduate_info',
            new_name='Education',
        ),
        migrations.RenameField(
            model_name='approval',
            old_name='email',
            new_name='Email',
        ),
        migrations.RenameField(
            model_name='approval',
            old_name='first_name',
            new_name='First_name',
        ),
        migrations.RenameField(
            model_name='approval',
            old_name='gender',
            new_name='Gender',
        ),
        migrations.RenameField(
            model_name='approval',
            old_name='last_name',
            new_name='Last_name',
        ),
        migrations.RenameField(
            model_name='approval',
            old_name='loan_amount',
            new_name='LoanAmount',
        ),
        migrations.RenameField(
            model_name='approval',
            old_name='loan_term',
            new_name='Loan_Amount_Term',
        ),
        migrations.RenameField(
            model_name='approval',
            old_name='married',
            new_name='Married',
        ),
        migrations.RenameField(
            model_name='approval',
            old_name='area',
            new_name='Property_Area',
        ),
        migrations.RenameField(
            model_name='approval',
            old_name='self_employed',
            new_name='Self_Employed',
        ),
    ]
