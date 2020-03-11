from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django import forms
from uuid import uuid4


# Create your models here.
class RegisteredUser(models.Model):
    Id = models.CharField(max_length=100, blank=True, unique=True, default=uuid4, primary_key=True)
    FirstName = models.CharField(max_length=30)
    LastName = models.CharField(max_length=50)
    Email = models.EmailField(max_length=100, default="<address>@domain.com")
    PhoneNumber = PhoneNumberField()


