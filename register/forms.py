from django import forms
#from phone_field import PhoneField
from .models import RegisteredUser
from django.core.exceptions import NON_FIELD_ERRORS
from phonenumber_field.modelfields import PhoneNumberField


class RegisterForm(forms.ModelForm):
    class Meta:
        model = RegisteredUser
        fields = ('FirstName', 'LastName', 'Email', 'PhoneNumber')

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        # add custom error messages
        self.fields['FirstName'].error_messages.update({
            'required': 'Please let us know what to call you!',
        })
