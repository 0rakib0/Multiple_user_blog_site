from django.db import models

from Auth_app.models import CustomUser

class Blog(models.Model):
    Author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='User_blog')
    Blog_title = models.CharField(max_length=267, verbose_name='Put a Title')
    Slug = models.SlugField(max_length=267, unique=True, blank=True)
    Blog_content = models.TextField()
    Blog_image = models.ImageField(upload_to='Blog_image')
    publish_date   = models.DateTimeField(auto_now_add=True)
    Update_date    = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-publish_date']
    
    
    def __str__(self) -> str:
        return self.Blog_title
    
class Comment(models.Model):
    Blog_comment = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='Blog_comment')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='User_comment')
    comment = models.TextField()
    Comment_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.comment
    
class Like(models.Model):
    Blog_like = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='Blog_like')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='User_like')
    
    
    def __str__(self) -> str:
        return str(self.user) +"like's" + str(self.Blog_like)