from django.shortcuts import redirect, render
from django.db.models import Q
from .models import Post, Topic, Major
from .forms import PostForm

# Create your views here.

def home(request):
    q = request.GET.get('q', '')
    posts = Post.objects.filter(
        Q(topic__name__icontains=q) |
        Q(title__icontains=q) |
        Q(body__icontains=q)
        )

    majors = Major.objects.all()
    topics = Topic.objects.all()
    post_count = posts.count()
    context = {'majors': majors, 'topics': topics, 'posts': posts, 'post_count': post_count}
    return render(request, 'base/home.html', context)

def post(request, id):
    post = Post.objects.get(id=id)
    context = {'post': post}
    return render(request, 'base/post.html', context)

def createPost(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/post_form.html', context)

def updatePost(request, id):
    post = Post.objects.get(id=id)
    form = PostForm(instance=post)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/post_form.html', context)

def deletePost(request, id):
    post = Post.objects.get(id=id)
    if request.method == 'POST':
        post.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj': post})