from django import forms
from django.forms import fields
from .models import Post, Comment
from posts import models

class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('body',)

class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('body',)

class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        widgets = {
            'body': forms.Textarea(attrs={'class':'form-control'})
        }

        error_messages = {
            'body':{
                'required' : 'این قسمت الزامی است',
            }
        }
        help_texts = {
            'body':'max 400 character',
        }

class AddReplyForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('body',)