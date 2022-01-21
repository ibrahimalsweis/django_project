from django.shortcuts import render ,get_object_or_404
from .models import Post,Comment
from .forms import commentsForm
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
    form_comment = commentsForm()



    context ={
        'title_page':post,
        'post':post,
        'comments':comments,
        'form_comment':form_comment,
    }
    if request.method == 'POST':
        comment_value =commentsForm(request.POST)
        if comment_value.is_valid:
            new_comment= comment_value.save(commit=False)
            new_comment.post = post
            new_comment.save()
            form_comment = commentsForm()
    return render(request,"blog/detail.html",context)
