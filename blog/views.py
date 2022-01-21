from multiprocessing import context
from django.shortcuts import render ,get_object_or_404
from .models import Post,Comment

def home(request):
    context ={
        'title_page':'الرئيسية',
        'posts':Post.objects.all()

    }
    return render(request,"blog/home.html",context)




def about(request):
    context ={
        'title_page':'أتصل بنا ',
    }
    return render(request,'blog/about.html',context)

def detail_post(request,post_id):
    post = get_object_or_404(Post,pk=post_id)
    comments = post.comments.all()
    context ={
        'title_page':post,
        'post':post,
        'comments':comments
    }
    return render(request,"blog/detail.html",context)
