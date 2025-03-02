from django.shortcuts import render,redirect,get_object_or_404,HttpResponse
from .models import PostModel,CategoryModel,CommentModel
from .forms import PostForm,EditPostForm,Category,CommentCreateForm
from bs4 import BeautifulSoup
from django.contrib.auth.decorators import login_required
import requests
# Create your views here.
titleName = 'TimeKeeper'
def home(request,tag=None):
    title = titleName
    posts = PostModel.objects.all()
    categorys = CategoryModel.objects.all()
    if tag is not None:
        posts = PostModel.objects.filter(category__slug=tag)
        tag = get_object_or_404(CategoryModel,slug=tag)
    
    context = {
        'title':title ,
        'posts':posts,
        'categorys':categorys,
        'tag':tag
        }
    return render(request,'post/home.html',context)
@login_required
def create_post(request):
    title = titleName
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            
            website = requests.get(form.data['url'])
            
            sourceCode = BeautifulSoup(website.text,'html.parser')
            
            find_image = sourceCode.select('meta[content^="https://live.staticflickr.com/"]')
            
            img = find_image[0]['content']
            post.image = img
            find_title = sourceCode.select('h1.photo-title')
            title = find_title[0].text.strip()
            post.title = title
            find_artist = sourceCode.select('a.owner-name')
            artist = find_artist[0].text.strip()
            post.artist = artist
            post.author = request.user
            post.save()
            form.save_m2m()
            return redirect('homepage')
    form = PostForm()
    return render(request,'post/create_post.html',{'form':form,'title':title})

@login_required
def delete_post(request,pk):
    post = get_object_or_404(PostModel,post_id=pk)
    if post.author == request.user:
        title = titleName
        if request.method == "POST":
            post.delete()
            return redirect("homepage")
        return render(request,'post/delete_post.html',{'post':post,'title':title})
    else:
        return redirect("homepage")
@login_required
def update_post(request,pk):
    post = get_object_or_404(PostModel,post_id=pk)
    if post.author == request.user:
        title = titleName
        form = EditPostForm(instance=post)
        if request.method == "POST":
            form = EditPostForm(request.POST, instance=post)
            if form.is_valid():
                form.save()    
                return redirect("homepage")
            else:
                print(form.errors)
        return render(request,'post/update_post.html',{'post':post,'title':title,'form':form})
    else:
        return redirect("homepage")
def view_post(request,pk):
    title = titleName
    post = get_object_or_404(PostModel,post_id=pk)
    commentform = CommentCreateForm()
    return render(request,'post/view_post.html',{'post':post,'title':title,'commentform':commentform})

@login_required
def comment_send(request,pk):
    post = get_object_or_404(PostModel,post_id=pk)
    print(post)
    if request.method == "POST":
        form = CommentCreateForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
        else:
            print(form.errors)
    return redirect('view-post',post.post_id)
    



# 
@login_required
def create_category(request):
    title = titleName
    if request.method == "POST":
        form = Category(request.POST  )
        if form.is_valid():
            form.save()
            return redirect("homepage")
    form = Category()
    return render(request,'post/create_category.html',{'title':title,'form':form})

# 
@login_required
def comment_delete(request,pk):
    comment = get_object_or_404(CommentModel,id=pk,user=request.user)
    if comment.user == request.user:
        title = titleName
        if request.method == "POST":
            comment.delete()
            return redirect("view-post",comment.post.post_id)
        return render(request,'post/delete_comment_post.html',{'comment':comment,'title':title})
    else:
        return redirect("view-post")
    
    
@login_required
def liked_post(request,pk):
    post =get_object_or_404(PostModel,post_id=pk)
    user_exist = post.liked.filter(username=request.user.username).exists()
    if user_exist:
        post.liked.remove(request.user)
    else:
        post.liked.add(request.user)
    
    return render(request,'snippet/likes.html',{'post':post})