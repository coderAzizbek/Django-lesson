from django.shortcuts import render
from django.views.generic import ListView,CreateView,DetailView,UpdateView
from .models import Post
# Create your views here.

class Yangilik(ListView):
    model = Post
    template_name = 'home.html'

class YangilikCraeteView(CreateView):
    model = Post
    template_name = 'create.html'
    fields = ['title','text','name']
class YangilikDetailView(DetailView):
    model = Post
    template_name = 'detail.html'

class YangilikUpdateView(UpdateView):
    model = Post
    template_name = 'update.html'
    fields = ['title','text']
