from django.db import models
import uuid
from django.utils.text import slugify
from django.contrib.auth.models import User
class CategoryModel(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=20,unique=True,blank=True)
    def __str__(self):
        return self.name
    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    class Meta:
        ordering = ["name"]
        

class PostModel(models.Model):
    post_id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    title = models.CharField(max_length=255)
    image = models.URLField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    # 
    url = models.URLField(null=True)
    artist = models.CharField(null=True)
    # 
    category = models.ManyToManyField(CategoryModel)
    author = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    # 
    liked = models.ManyToManyField(User,related_name='LikePost',through="LikePost")
    def __str__(self):
        return f"{self.post_id}: {self.title}"
    class Meta:
        ordering = ["-created"]
        
class LikePost(models.Model):
    post = models.ForeignKey(PostModel,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username}: {self.post.title} "
           
        
class CommentModel(models.Model):
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='comments')
    body = models.CharField(max_length=150)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return f"{self.user.username if self.user else 'deleted_user'}: {self.body}"
    
    class Meta:
        ordering = ["-created"]