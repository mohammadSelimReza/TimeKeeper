from django.shortcuts import render,redirect,get_object_or_404
from .forms import ProfileForm
from django.contrib.auth import logout
from django.contrib.auth.models import User
# Create your views here.
def profile_view(request):
    profile = request.user.profilemodel
    print(profile)
    return render(request,'user/profile.html',{'profile':profile})


def profile_edit(request):
    form = ProfileForm(instance=request.user.profilemodel)
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES ,instance=request.user.profilemodel)
        if form.is_valid():
            form.save()
            return redirect("profile_view")
        else:
            print(form.errors)
    return render(request,'user/profile_edit.html',{'form':form})

def profile_delete(request):
    user = request.user
    print(user)
    if request.method == "POST":
        logout(request)
        user.delete()
        return redirect("homepage")
    return render(request,'user/profile_delete.html')