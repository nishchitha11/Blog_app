from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm
from django.urls import reverse_lazy

#For Home Page
class HomeView(ListView):
    model = Post
    template_name = 'home.html'

#For Article Page
class ArticleDetailView(DetailView):
    model = Post
    template_name = "article_details.html"

#To ADD BLOG
class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'

#To UPDATE and EDIT BLOG
class UpdatePostView(UpdateView):
    model = Post
    template_name = 'update_post.html'
    fields = ['title', 'title_tag', 'body']

#To DELETE BLOG
class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
