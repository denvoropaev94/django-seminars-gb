from django.shortcuts import render, get_object_or_404
from .models import Authors, Posts, Comment


def index(request):
    return render(request, 'sem3/index.html')


def about(request):
    return render(request, 'sem3/about.html')


def author_posts(request, author_id):
    author = get_object_or_404(Authors, pk=author_id)
    posts = Posts.objects.filter(author=author)
    return render(request, 'sem3/author_post.html', {'author': author, 'posts': posts})


def post_view(request, post_id):
    post = get_object_or_404(Posts, pk=post_id)
    return render(request, 'sem3/post_view.html', {'post': post})
