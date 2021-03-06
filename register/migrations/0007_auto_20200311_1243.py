# Generated by Django 3.0.2 on 2020-03-11 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0006_auto_20200311_1209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registereduser',
            name='Email',
            field=models.EmailField(error_messages={'unique': 'This email already exists.'}, max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='registereduser',
            name='FirstName',
            field=models.CharField(error_messages={'required': 'Please enter your first name'}, max_length=30),
        ),
        migrations.AlterField(
            model_name='registereduser',
            name='LastName',
            field=models.CharField(error_messages={'required': 'Please enter your last name'}, max_length=50),
        ),
    ]
