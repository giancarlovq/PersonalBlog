from .models import Contact
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.forms import ModelForm


class ContactForm(ModelForm):

    helper = FormHelper()
    helper.form_id = 'id_contact_Form'
    helper.form_class = 'blueForms'
    helper.form_method = 'post'
    helper.form_action = 'submit_survey'

    helper.add_input(Submit('submit', 'Submit'))


    class Meta:
        model = Contact

        fields = [
            'user_name',
            'email_address',
            'massage',
            ]

        labels = {
            'user_name': 'Full Name',
            'email_address': 'Email',
            'massage': 'Content',
            }
