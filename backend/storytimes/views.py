from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Prompt, Post, Chapter, Comment
from .forms import PromptForm, PostForm

def prompt_list(request):
    prompts = Prompt.objects.all()
    return render(request, 'storytimes/prompt_list.html', {'prompts': prompts})

def prompt_detail(request, id):
    prompt = Prompt.objects.get(id=id)
    return render(request, 'storytimes/prompt_detail.html', {'prompt': prompt})

@login_required
def prompt_create(request):
    if request.method == 'POST':
        form = PromptForm(request.POST)
        if form.is_valid():
            prompt = form.save()
            return redirect('prompt_detail', id=prompt.id)
    else:
        form = PromptForm()
    return render(request, 'storytimes/prompt_create.html', {'form': form})

@login_required
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

@login_required
def prompt_delete(request, id):
    prompt = Prompt.objects.get(id=id).delete()
    return redirect('prompt_list')

def post_detail(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'storytimes/post_detail.html', {'post': post})

@login_required
def post_create(request, id):
    prompt = Prompt.objects.get(id=id)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('post_detail', id=post.id)
    else:
        form = PostForm()
        form.fields['prompt'].initial = prompt
    return render(request, 'storytimes/post_create.html', {'form': form})

@login_required
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

@login_required
def post_delete(request, id):
    prompt = Post.objects.get(id=id).delete()
    return redirect('prompt_detail')