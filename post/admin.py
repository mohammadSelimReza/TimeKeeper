from django.contrib import admin
from .models import PostModel,CategoryModel,CommentModel,LikePost
# Register your models here.
admin.site.register(PostModel)
admin.site.register(CategoryModel)
admin.site.register(CommentModel)
admin.site.register(LikePost)