from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django import forms
from uuid import uuid4


# Create your models here.
class RegisteredUser(models.Model):
    Id = models.CharField(max_length=100, blank=True, unique=True, default=uuid4, primary_key=True)
    FirstName = models.CharField(max_length=30,
                                 error_messages={
                                     'required': 'Please enter your first name'
                                 },
                                 blank=False)
    LastName = models.CharField(max_length=50,
                                error_messages={
                                    'required': 'Please enter your last name'
                                },
                                blank=False)
    Email = models.EmailField(
        max_length=100,
        unique=True,
        blank=False,
        error_messages={"unique": "This email already exists."})
    PhoneNumber = PhoneNumberField()
