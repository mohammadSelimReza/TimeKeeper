from django.dispatch import receiver
from django.shortcuts import get_object_or_404
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import ProfileModel


@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
    if created:
        ProfileModel.objects.create(
            user = instance,
            email = instance.email,
        )
    else:
        profile = get_object_or_404(ProfileModel,user=instance)
        profile.email = instance.email
        profile.save()
        
@receiver(post_save,sender=ProfileModel)
def update_user(sender,instance,created,**kwargs):
    profile = instance
    if created ==False:
        user = get_object_or_404(User,id=profile.user.id)
        if user.email != profile.email:
            user.email = profile.email
            user.save()