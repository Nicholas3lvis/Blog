from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=11, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    residence = models.CharField(max_length=100, blank=True, null=True)
    yearofbirth= models.DateField(blank=True, null=True)
    created = models.DateField(blank=True, null=True)
    # updated = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    profile_pic = models.ImageField(upload_to='user_img', blank=True, null=True)
    SERVICE_TYPE =[('Available for freelance','freelance'),('Not available for freelance','job')]
    freelance = models.CharField(max_length=50, choices=SERVICE_TYPE, blank=True, null=True )
    social_link = models.URLField(max_length=100, blank=True, null=True)
    core_skill = models.CharField(max_length=50, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS= 'username', "first_name"
    
    def __str__(self):
        return self.email
