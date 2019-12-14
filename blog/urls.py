from django.urls import path
from . import views


urlpatterns = [
    path('', views.blog_start_cards, name = 'blog_start_cards'),
    path('blog/', views.blog_post_pages, name = 'blog_post_pages'),
    ]
