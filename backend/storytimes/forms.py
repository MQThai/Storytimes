from django import forms
from .models import Prompt, Post, Comment

class PromptForm(forms.ModelForm):
    class Meta:
        model = Prompt
        fields = ('author', 'body',)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('prompt', 'author', 'title', 'body',)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('post', 'user', 'body',)