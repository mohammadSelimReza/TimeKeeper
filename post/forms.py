from django import forms
from .models import PostModel,CategoryModel,CommentModel

class PostForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = ['url','body','category']
        label = {
            'body':"Caption",
            'category': 'Category',
        }
        widgets ={
            'body' : forms.Textarea(attrs={'row':3,'placeholder':'Add a caption...','class':'font1 text-4xl h-40'}),
            'url' : forms.TextInput(attrs={'placeholder':'Add url......'}),
            'category': forms.CheckboxSelectMultiple(attrs={'class': 'custom-checkbox'}),
        }
class EditPostForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = ['body','category']
        label = {
            'body':'',
            'category': 'Category',
        }
        widgets ={
            'body' : forms.Textarea(attrs={'row':3,'class':'font1 text-4xl h-40'}),
            'category': forms.CheckboxSelectMultiple(attrs={'class': 'custom-checkbox'}),
        }
class Category(forms.ModelForm):
    class Meta:
        model = CategoryModel
        fields = ['name',]
        widgets ={
           'name' : forms.TextInput(attrs={'placeholder':'Add new category......'}),
        }
        
class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        fields = ['body']
        widgets = {
            'body': forms.TextInput(attrs={'placeholder':'Add Comment...',})
        }
        label ={
            'body':'',
        }