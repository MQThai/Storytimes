from django import forms
from .models import Prompt, Post, Chapter, Comment

class PromptForm(forms.ModelForm):
    class Meta:
        model = Prompt
        fields = ('body',)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body',)