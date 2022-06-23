from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView
from django.views.generic.detail import DetailView
from django.urls import reverse,reverse_lazy
from django.shortcuts import render
from .models import Post

# Create your views here
class PostListView(ListView):
    model = Post
    template_name = "base.html"

class PostCreateView(CreateView):
    model=Post
    fields="__all__"
    success_url = reverse_lazy("blog:all")

class PostDetailView(DetailView):
    model = Post
    template_name = ".html"

class PostUpdateView(UpdateView):
    model = Post
    fields="__all__"
    success_url=reverse_lazy("blog:all")
    template_name = ".html"

class PostDeleteView(UpdateView):
    model = Post
    fields="__all__"
    success_url=reverse_lazy("blog:all")
    template_name = ".html"









