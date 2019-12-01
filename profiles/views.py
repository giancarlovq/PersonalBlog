from django.views.generic import TemplateView


# Create your views here.
class Register(TemplateView):
    template_name = 'profiles/register.html'
