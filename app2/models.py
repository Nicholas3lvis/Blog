from django.db import models
from django.conf import settings
from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=200)
    
    def __str__(self):
        return self.title


class Blog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True, related_name='blogs')
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField()
    body = CKEditor5Field(blank=True,null=True)
    # body = models.TextField()
    img = models.ImageField(upload_to='img')
    created = models.DateTimeField(auto_now_add =True)
    updated = models.DateTimeField(auto_now_add =True)
    featured = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='blogs', blank=True, null=True)
    
    
    def __str__(self):
        return f'{self.author}  - {self.title}'
    
class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, blank=True, null=True, related_name='comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True, related_name='comments')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add =True)
    
    def __str__(self):
        return self.body
    
