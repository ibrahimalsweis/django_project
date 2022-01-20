from django.shortcuts import render
from .models import Post


def home(request):
    context ={
        'title_page':'الرئيسية',
        'posts':Post.objects.all()

    }
    return render(request,"blog/home.html",context)




def about(request):
    context ={
        'title_page':'أتصل بنا ',
        'posts':Post.objects.all()

    }
    return render(request,'blog/about.html',context)