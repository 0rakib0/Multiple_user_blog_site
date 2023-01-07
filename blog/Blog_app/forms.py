from dataclasses import fields
from pyexpat import model
from django import forms
from .models import Blog, Comment


class Comment_form(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']