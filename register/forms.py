from django import forms
from phone_field import PhoneField
from .models import RegisteredUser

class RegisterForm(forms.ModelForm):
    class Meta:
        model = RegisteredUser
        fields = ('FirstName', 'LastName', 'Email', 'PhoneNumber')
