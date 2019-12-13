from django.shortcuts import render
from .models import Publication


# Create your views here.
def blog(request):
    publications = Publication.objects.all()
    return render(request, 'blog/blog.html', {'publications': publications})
