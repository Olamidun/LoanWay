# Generated by Django 3.2.6 on 2021-08-31 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loanway_app', '0012_approval_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='approval',
            name='eligibility_status',
            field=models.BooleanField(default=False),
        ),
    ]