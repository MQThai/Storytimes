from django.urls import path
from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from . import views

urlpatterns = [
    path('prompts', views.PromptList.as_view(), name='prompt-list'),
    path('prompts/<int:pk>', views.PromptDetail.as_view(), name='prompt-detail'),
    path('posts', views.PostList.as_view(), name='post-list'),
    path('posts/<int:pk>', views.PostDetail.as_view(), name='post-detail'),
    path('chapters', views.ChapterList.as_view(), name='chapter-list'),
    path('chapters/<int:pk>', views.ChapterDetail.as_view(), name='chapter-detail'),
    path('comments', views.CommentList.as_view(), name='comment-list'),
    path('comments/<int:pk>', views.CommentDetail.as_view(), name='comment-detail')
]