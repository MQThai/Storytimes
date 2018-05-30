from django.shortcuts import render, redirect
from rest_framework import generics
from .serializers import PromptSerializer, PostSerializer, ChapterSerializer, CommentSerializer
from .models import Prompt, Post, Chapter, Comment
from .forms import PromptForm, PostForm

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

def prompt_list(request):
    prompts = Prompt.objects.all()
    return render(request, 'storytimes/prompt_list.html', {'prompts': prompts})

def prompt_detail(request, id):
    prompt = Prompt.objects.get(id=id)
    return render(request, 'storytimes/prompt_detail.html', {'prompt': prompt})

def prompt_create(request):
    if request.method == 'POST':
        form = PromptForm(request.POST)
        if form.is_valid():
            prompt = form.save()
            return redirect('prompt_detail', id=prompt.id)
    else:
        form = PromptForm()
    return render(request, 'storytimes/prompt_create.html', {'form': form})

def prompt_edit(request, id):
    prompt = Prompt.objects.get(id=id)
    if request.method == 'POST':
        form = PromptForm(request.POST, instance=prompt)
        if form.is_valid():
            prompt = form.save()
            return redirect('prompt_detail', id=prompt.id)
    else:
        form = PromptForm(instance=prompt)
    return render(request, 'storytimes/prompt_create.html', {'form': form})

def prompt_delete(request, id):
    prompt = Prompt.objects.get(id=id).delete()
    return redirect('prompt_list')

def post_detail(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'storytimes/post_detail.html', {'post': post})

def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('post.detail', id=post.id)
    else:
        form = PostForm()
    return render(request, 'storytimes/post_create.html', {'form': form})

def post_edit(request, id):
    post = Post.objects.get(id=id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect('post_detail', id=post.id)
    else:
        form = PostForm(instance=post)
    return render(request, 'storytimes/post_create.html', {'form': form})