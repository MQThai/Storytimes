from django import forms
from .models import Prompt, Post

class PromptForm(forms.ModelForm):
    class Meta:
        model = Prompt
        fields = ('author', 'body',)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('prompt', 'title', 'body',)