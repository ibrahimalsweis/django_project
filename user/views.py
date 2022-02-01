
from django.shortcuts import render,redirect

from django.contrib import messages
from .forms import createUser
from blog.models import Post
def register(request):
    if request.method == 'POST':
       form = createUser(request.POST)
       if form.is_valid():
           form.save()
           first_name = form.cleaned_data['first_name']
           last_name = form.cleaned_data['last_name']
           messages.success(request,f'تم انشاء الحساب بنجاح مرحباً {first_name} {last_name}')
           return redirect("login")
    else:
       form = createUser()
    return render(request ,'user/register.html',{
        'title_page':'أنشاء حساب جديد',
        'form':form,
    })

def profile(request):
    posts_user = Post.objects.filter(author=request.user)
    return render(request,'user/profile.html',{
        'title_page':'الملف الشحصي',
        'posts':posts_user,
    })