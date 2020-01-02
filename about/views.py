""" View Detail. """

# Django
from django.views.generic import TemplateView
from django.shortcuts import render

# Local | Model
from .models import About


# Create your views here.
class AboutView(TemplateView):
    """
    Template View: About me.
    """

    template_name = 'about/about.html'
    model_about = About.objects.all()

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'model_about': self.model_about})
