# Generated by Django 3.2.6 on 2021-09-02 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loanway_app', '0015_alter_approval_dependents'),
    ]

    operations = [
        migrations.AlterField(
            model_name='approval',
            name='Dependents',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('3+', '3+')], max_length=2),
        ),
    ]
