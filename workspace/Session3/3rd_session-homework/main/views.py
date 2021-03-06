from django.shortcuts import render,get_object_or_404, redirect
from .models import Post
from django.utils import timezone

# mainpage view 함수
def showmain(request):
    posts = Post.objects.all()
    return render(request, 'main/hwpresent.html', {'posts':posts})

def new(request):
    return render(request, 'main/new.html')

def create(request):
    new_post = Post()
    new_post.title = request.POST['title']
    new_post.writer = request.POST['writer']
    new_post.pub_date = timezone.now()
    new_post.body = request.POST['body']
    new_post.save()
    return redirect('detail',new_post.id)

def detail(request,id):
    post = get_object_or_404(Post, pk = id)
    return render(request, 'main/detail.html', {'post':post})

