from django.urls import path
from .views import BlogCardsList, BlogPagesDetail


urlpatterns = [
    path('', BlogCardsList.as_view(), name = 'blog_cards_list'),
    path('blog/<int:pk>/<slug:slug>/', BlogPagesDetail.as_view(), name = 'blog_pages_detail'),
    ]
