from pyexpat import model
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

from . models import Post

# Create your views here.

class BlogHomeView(ListView):
    template_name = "blog/blog-home.html"
    model = Post
    context_object_name = "posts"
    ordering = ["-date"]

    def get_queryset(self):
        queryset = super().get_queryset()
        latest_posts = queryset[:3]
        return latest_posts

