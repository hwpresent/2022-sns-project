from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from django.utils import timezone


# mainpage view 함수
def showmain(request):
    blogs = Blog.objects.all()
    return render(request, 'main/mainpage.html', {'blogs':blogs})

# firstpage view 함수
def showfirst(request):
    return render(request, 'main/firstpage.html')

# secondpage view 함수
def showsecond(request):
    return render(request, 'main/secondpage.html')

def detail(request, id):
    blog = get_object_or_404(Blog, pk = id)
    return render(request, 'main/detail.html', {'blog':blog})

def new(request):
    return render(request, 'main/new.html')

def create(request):
    new_blog = Blog()
    new_blog.title = request.POST['title']
    new_blog.writer = request.POST['writer']
    new_blog.pub_date = timezone.now()
    new_blog.body = request.POST['body']
    new_blog.save()
    return redirect('detail', new_blog.id)