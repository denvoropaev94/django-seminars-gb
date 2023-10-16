from .views import index, about, author_posts, post_view
from django.urls import path

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('author_posts/<int:author_id>', author_posts, name='author_posts'),
    path('post/<int:post_id>', post_view, name='post_view'),
]
