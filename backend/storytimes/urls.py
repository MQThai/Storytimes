from django.urls import path
from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from . import views

urlpatterns = [
    path('', views.prompt_list, name='prompt_list'),
    path('about', views.about, name='about'),
    path('prompts/<int:id>', views.prompt_detail, name='prompt_detail'),
    path('prompts/new', views.prompt_create, name='prompt_create'),
    path('prompts/<int:id>/edit', views.prompt_edit, name='prompt_edit'),
    path('prompts/<int:id>/delete', views.prompt_delete, name='prompt_delete'),
    path('posts/<int:id>', views.post_detail, name='post_detail'),
    path('prompts/<int:id>/posts/new', views.post_create, name='post_create'),
    path('posts/<int:id>/edit', views.post_edit, name='post_edit'),
    path('posts/<int:id>/delete', views.post_delete, name='post_delete'),
]