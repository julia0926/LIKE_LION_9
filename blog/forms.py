from django import forms
from django.forms import models
from .models import Blog,Comment, Hashtag

class PostForm(forms.ModelForm):
    class Meta:
        model = Blog #Blog 모델을 참조해서 model을 만듬 
        fields = ['title', 'writer','content','image','hashtags'] #모델 값은 이러함.

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

class HashtagForm(forms.ModelForm):
    class Meta:
        model = Hashtag
        fields = ['name']