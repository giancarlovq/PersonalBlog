from .models import SocialNetwork


def context_processors(request):
    context = {}
    links = SocialNetwork.objects.all()

    for link in links:
        context[link.key] = link.url

    return context
