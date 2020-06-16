from django.shortcuts import render
from django.views.generic import TemplateView,ListView, DetailView
from .models import Post

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

class ListView(ListView):
    template_name = 'post_detail.html'
    model = Post

class ListView(DetailView):
    template_name = 'post_detail.html'
    model = Post
