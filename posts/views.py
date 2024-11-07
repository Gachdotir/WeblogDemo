from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.views import generic
from rest_framework.decorators import api_view
from rest_framework.response import Response

from posts.models import Post, Comment
from .forms import PostForm


@api_view(["GET"])
def index(request):
    # return HttpResponse('<h1>Welcome to my weblog!</h1>')
    return Response({'hello'})


def home(request):
    return HttpResponse('<h3>Welcome to my Blog...</h3>')

    # def post_list(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'posts/post_list.html', context=context)


class PostList(generic.ListView):
    queryset = Post.objects.all()
    template_name = 'posts/post_list.html'
    context_object_name = 'posts'


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comment = Comment.objects.filter(post=post)
    context = {'post': post, 'comment': comment}
    return render(request, 'posts/post_detail.html', context=context)


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'posts/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data()
        context['comments'] = Comment.objects.filter(post=kwargs['object'].pk)


def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            Post.objects.create(**form.cleaned_data)
            return HttpResponseRedirect('/posts/')
    else:
        form = PostForm()

    return render(request, 'posts/post_create.html', {'form': form})
