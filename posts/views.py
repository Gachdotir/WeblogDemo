from django.shortcuts import render
from django.http import HttpResponse

from posts.models import Post, Comment


def index(request):
    return HttpResponse('<h1>Welcome to my weblog!</h1>')


def home(request):
    return HttpResponse('<h3>Welcome to my Blog...</h3>')


def post_list(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'posts/post_list.html', context=context)


def post_detail(request, post_id):
    post = Post.objects.get(pk=post_id)
    comment = Comment.objects.filter(post=post)
    context = {'post': post, 'comment': comment}
    return render(request, 'posts/post_detail.html', context=context)