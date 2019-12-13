from django.contrib.auth import login, authenticate
from django.views.generic import TemplateView
from django.shortcuts import render
from .forms import UserRegisterForm


# Create your views here.
class RegisterView(TemplateView):

    register_form_class = UserRegisterForm
    template_name = 'profiles/register.html'

    def get(self, request, *args, **kwargs):
        form = self.register_form_class
        return render(request, self.template_name, {'form': form})

    
