from django.shortcuts import render
from .models import Publication


# Create your views here.
def blog_start_cards(request):
    publications = Publication.objects.all()
    return render(request, 'blog/blogstartcards.html', {'publications': publications})

def blog_post_pages(request):
    publications = Publication.objects.all()
    return render(request, 'blog/blogpostpages.html', {'publications': publications})
