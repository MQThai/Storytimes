from django.urls import path
from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from . import views

urlpatterns = [
    path('', views.prompt_list, name='prompt_list'),
    path('prompts/<int:id>', views.prompt_detail, name='prompt_detail'),
    path('posts/<int:id>', views.post_detail, name='post_detail'),
    path('chapters', views.ChapterList.as_view(), name='chapter_list'),
    path('chapters/<int:id>', views.ChapterDetail.as_view(), name='chapter_detail'),
    path('comments', views.CommentList.as_view(), name='comment_list'),
    path('comments/<int:id>', views.CommentDetail.as_view(), name='comment_detail')
]