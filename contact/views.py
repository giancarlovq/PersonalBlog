""" Form View """

# Django
from django.shortcuts import render, redirect
from django.urls import reverse
# Django | Mixin
from django.views.generic.edit import ProcessFormView
# Django | Send Message
from django.core.mail import EmailMessage

# Local | ModelForm
from .forms import ContactForm


# Create your views here.
class Contact(ProcessFormView):
    """
    Class Contact View.
    """
    template_name = 'contact/contact.html'
    contact_form = ContactForm

    def get(self, request, *args, **kwargs):
        """
        Render form in the template.
        """
        return render(request, self.template_name, {'form': self.contact_form})

    def post(self, request, *args, **kwargs):
        """
        Valid that the request method is POST.
        """
        if request.method == 'POST':
            self.contact_form = ContactForm(data = request.POST)

            if self.contact_form.is_valid():
                user_name = request.POST.get('user_name', '')
                email_address = request.POST.get('email_address', '')
                message = request.POST.get('message', '')

                self.contact_form.save()

                email_message = EmailMessage(
                        # Subject
                        'Personal Blog: New test message.',
                        # Message
                        f'From: {user_name} \nEmail: {email_address} \nMessage: {message}',
                        # From Email
                        'no-answer@inbox.mailtrap.io',
                        # Email Receiver
                        ['giancarlovq@outlook.es'],
                        # Reply to
                        reply_to = [email_address]
                        )

                # Send email
                try:
                    # Sample message: 'Sent satisfactory.'
                    email_message.send()
                    return redirect(reverse('contact') + '?Success')
                except:
                    return redirect(reverse('contact') + '?Failed')


        return redirect(reverse('contact'))
