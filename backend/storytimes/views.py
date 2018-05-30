from django.shortcuts import render
from rest_framework import generics
from .serializers import PromptSerializer, PostSerializer, ChapterSerializer, CommentSerializer
from .models import Prompt, Post, Chapter, Comment

class PromptList(generics.ListCreateAPIView):
    queryset = Prompt.objects.all()
    serializer_class = PromptSerializer

class PromptDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Prompt.objects.all()
    serializer_class = PromptSerializer

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class ChapterList(generics.ListCreateAPIView):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer

class ChapterDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer

class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer