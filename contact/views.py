from .forms import ContactForm
from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class Contact(TemplateView):
    contact_form = ContactForm
    template_name = 'contact/contact.html'

    def get(self, request, *args, **kwargs):
        form = self.contact_form
        return render(request, self.template_name, {'form': form})
