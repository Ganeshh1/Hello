from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.
def home(request):
    
    content={
        'posts':Post.objects.all(),
    }
    return render(request,'Post/home.html',content)

def about(request):
    content={
        'Student':Post.objects.all()[0],
    }
    return render(request,'Post/Resume.html',content)