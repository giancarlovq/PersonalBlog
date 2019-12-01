from django.views.generic import TemplateView

# Create your views here.
class Login(TemplateView):
    template_name = 'login/login.html'

