# Generated by Django 3.2.6 on 2021-08-29 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loanway_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='approval',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
