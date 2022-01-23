from django.shortcuts import render ,get_object_or_404
from .models import Post,Comment
from .forms import commentsForm
def home(request):
    context ={
        'title_page':'الرئيسية',
        'posts':Post.objects.all(),
        # 'comments':comments,

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
    form_comment = commentsForm()

    if request.method == 'POST':
        form_comment =commentsForm(data=request.POST)
        if form_comment.is_valid:
            new_comment= form_comment.save(commit=False)
            new_comment.post = post
            new_comment.save()
            form_comment = commentsForm()
    else:
        form_comment = commentsForm()
    context ={
        'title_page':post,
        'post':post,
        'comments':comments,
        'form_comment':form_comment,
    }


    return render(request,"blog/detail.html",context)
