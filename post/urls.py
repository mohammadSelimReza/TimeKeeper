from django.urls import path
from . import views
urlpatterns = [
    path("",views.home,name="homepage"),
    path("add/post/",views.create_post,name="add-post"),
    path("post/view/<pk>/",views.view_post,name="view-post"),
    path("post/update/<pk>/",views.update_post,name="update-post"),
    path("post/delete/<pk>/",views.delete_post,name="delete-post"),
    path("category/create/",views.create_category,name="category-add"),
    path("category/<tag>/",views.home,name="category-list"),
    path("post/comment/add",views.home,name="addComment"),
    path("post/comment/add/<pk>",views.comment_send,name="newComment"),
    path("post/comment/delete/<pk>",views.comment_delete,name="deleteComment"),
    path("post/like/<pk>",views.liked_post,name="likePost"),
]
