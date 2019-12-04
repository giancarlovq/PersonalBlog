from django.forms import ModelForm
from .models import UserRegister


# Creating Form for Register
class UserRegisterForm(ModelForm):

    class Meta:
        model = UserRegister

        fields = [
            'first_name',
            'last_name',
            'email_address',
            'password',
            ]

        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email_address': 'Email Address',
            'password': 'Password',
            }

