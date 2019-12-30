""" Contact Model Based Form. """

# Django
from django.forms import ModelForm, Textarea
# Django Form
from django.forms import Textarea

# Local | Model > Contact
from .models import Contact


class ContactForm(ModelForm):
    """
     Form inherits from the ModelForm model.
    """

    class Meta:
        model = Contact

        fields = [
            'user_name',
            'email_address',
            'message',
            ]

        labels = {
            'user_name': 'Full Name',
            'email_address': 'Email',
            'message': 'Content',
            }

        # Overwrite the default field of the model.
        # Represented 'TextField' by a 'Textarea'.
        widgets = {
            'message': Textarea(attrs = {'rows': 4}),
            }
