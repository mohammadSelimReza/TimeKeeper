from django import forms
from .models import ProfileModel

class ProfileForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = [ 
                "image",
                "full_name",
                "email",
                "location",
                "bio",
]
        widgets = {
            'image' : forms.FileInput(),
            'bio': forms.Textarea(attrs={'row':3})
        }