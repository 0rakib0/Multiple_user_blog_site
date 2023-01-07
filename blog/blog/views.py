from multiprocessing import context
from pyexpat import model
from django.shortcuts import render, redirect
from django.contrib import messages
from Blog_app.models import Blog



def home(request):
    blog_data = Blog.objects.all()
    blog_recent = Blog.objects.order_by('-id')[0:3]
    context = {
        'blog_data':blog_data,
        'blog_recent':blog_recent
    }
    return render(request, 'Blog/home.html', context)
