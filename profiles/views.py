from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView
from django.shortcuts import render
from .forms import UserRegisterForm


# Create your views here.
class Register(TemplateView):

    user_register = UserRegisterForm
    initial = {'key': 'value'}
    template_name = 'profiles/register.html'

    def get(self, request, *args, **kwargs):
        form = self.user_register(initial = self.initial)
        return render(request, self.template_name, {'form': form})
