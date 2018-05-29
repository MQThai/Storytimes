from django.contrib import admin
from .models import Prompt, Post, Chapter, Comment

# Register your models here.
admin.site.register([Prompt, Post, Chapter, Comment])