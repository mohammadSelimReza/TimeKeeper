from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class ProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/profile/',null=True,blank=True, default='profile/default_user.svg')
    full_name = models.CharField(max_length=30,null=True,blank=True)
    email = models.EmailField(max_length=50,null=True,blank=True)
    location = models.CharField(max_length=100,null=True,blank=True)
    bio = models.TextField(null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Profile of {self.full_name}"
    
    def save(self,*args, **kwargs):
        if self.email == "" or self.email == None:
            self.email = self.user.email
        super().save(*args, **kwargs)