from django.shortcuts import render, HttpResponse
from .models import Blog

# Create your views here.
def allblogs(request):
    context = {}
    blogs = Blog.objects.all()
    context['blogs'] = blogs
    return render(request, 'blog/allblogs.html', context)

def detail(request, blog_id):
    return HttpResponse('Hi')