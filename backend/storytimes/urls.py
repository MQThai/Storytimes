from django.urls import path
from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from . import views

urlpatterns = [
    path('', views.prompt_list, name='prompt_list'),
    path('prompts/<int:id>', views.prompt_detail, name='prompt_detail'),
    path('prompts/new', views.prompt_create, name='prompt_create'),
    path('prompts/<int:id>/edit', views.prompt_edit, name='prompt_edit'),
    path('prompts/<int:id>/delete', views.prompt_delete, name='prompt_delete'),
    path('posts/<int:id>', views.post_detail, name='post_detail'),
    path('posts/new', views.post_create, name='post_create'),
    path('posts/<int:id>/edit', views.post_edit, name='post_edit'),
    path('chapters', views.ChapterList.as_view(), name='chapter_list'),
    path('chapters/<int:id>', views.ChapterDetail.as_view(), name='chapter_detail'),
    path('comments', views.CommentList.as_view(), name='comment_list'),
    path('comments/<int:id>', views.CommentDetail.as_view(), name='comment_detail')
]