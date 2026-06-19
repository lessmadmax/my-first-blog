from urllib import request
from django.shortcuts import redirect
from django.shortcuts import render
from django.utils import timezone

from blog.froms import PostForm
from blog.serializers import PostSerializer
from .models import Post
from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from .serializers import PostSerializer

def post_list(request):
    posts = Post.objects.all()
    print("게시글 개수:", posts.count())  # 터미널에 숫자가 0으로 나오는지 확인!
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
    
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

class IntruderImage(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

