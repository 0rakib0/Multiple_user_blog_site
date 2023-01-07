from operator import ipow
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    gender = models.CharField(max_length=30)
    profile_pic = models.ImageField(upload_to='profile_pic')
    
    def __str__(self) -> str:
        return self.username
