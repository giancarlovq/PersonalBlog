""" View List and Detail. """

# Django
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

# Local | Model
from .models import Publication, BlogInformation


# Create your views here.
class BlogCardsList(ListView):
    """
    shown in the information inside the cards in the 'home'.
    Location: Home > cards
    """

    model = Publication

    def get_context_data(self, *, object_list=None, **kwargs):
        """
        Show information about the blog.
        Location: Home > jumbotron
        """
        context_blog_info = super().get_context_data(**kwargs)
        context_blog_info['blog_info'] = BlogInformation.objects.all()
        return context_blog_info


class BlogPagesDetail(DetailView):
    """
    Detailed view of each publication.
    """

    model = Publication
