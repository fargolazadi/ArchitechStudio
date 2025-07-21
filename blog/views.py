from django.shortcuts import render,get_object_or_404
from blog.models import *
# Create your views here.
def blog_index(request):
    posts = Blog.objects.all()
    context = {'posts':posts}
    return render(request,'blog.html',context)


def blog_persian_index(request):
    posts = Blog_persian.objects.all()
    context = {'posts':posts}
    return render(request,'blog-persian.html',context)



def blog_detail(request,pid):
    news = get_object_or_404(Blog,pk=pid)
    images = news.images.all()
    context = {'news':news,'images':images}
    return render(request,'blog-detail.html',context)


def blog_persian_detail(request,pid):
    news = get_object_or_404(Blog_persian,pk=pid)
    images = news.images.all()
    context = {'news':news,'images':images}
    return render(request,'blog-persian-detail.html',context)