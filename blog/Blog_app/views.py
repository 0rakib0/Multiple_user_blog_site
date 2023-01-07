from inspect import BlockFinder
from multiprocessing import context
from unicodedata import name
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import CustomUser
from .models import Blog, Like, Comment
from .forms import Comment_form
from django.urls import reverse
from django.http import HttpResponseRedirect
import uuid

# Create your views here.

def Blog_create(request):
    User = CustomUser.objects.all()
    if request.method == 'POST':
        title = request.POST.get('title')
        blog_img = request.FILES.get('blog_img')
        blog_content = request.POST.get('blog_content')
        
        blog = Blog(
            Blog_title = title,
            Blog_image = blog_img,
            Blog_content = blog_content,
        )
        blog.Author = request.user
        titles = blog.Blog_title
        blog.Slug = titles.replace(' ', '-')+ '-' + str(uuid.uuid4())
        blog.save()
        # messenge
        return redirect('home')
    context = {}
    return render(request, 'Blog/create_blog.html', context)


def Blog_details(request, slug):
    blog_data = Blog.objects.get(Slug=slug)
    comment_form = Comment_form()
    if request.method == 'POST':
        comment_form = Comment_form(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.Blog_comment = blog_data
            comment.save()
            return HttpResponseRedirect(reverse('Blog_app:blog_details', kwargs={'slug':slug}))
    context = {
        'blog_data':blog_data,
        'comment_form':comment_form
    }
    return render(request, 'Blog/blog_details.html', context)

def Edit_blog(request, id):
    blog = Blog.objects.get(id=id)
    context = {
        'blog':blog
    }
    return render(request, 'Blog/edit_blog.html', context)

def Update_blog(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        blog_id = request.POST.get('blog_id')
        blog_img = request.FILES.get('blog_img')
        blog_content = request.POST.get('blog_content')
        
        blog = Blog.objects.get(id=blog_id)
        blog.Blog_title = title
        blog.Blog_content = blog_content
        
        if blog_img !=None and blog_img !='':
            blog.Blog_image = blog_img
        
        blog.Author = request.user
        titles = blog.Blog_title
        blog.Slug = titles.replace(' ', '-')+ '-' + str(uuid.uuid4())
        blog.save()
        return redirect('Auth_app:profile')
        
        
    return render(request, 'Blog/edit_blog.html', context={})