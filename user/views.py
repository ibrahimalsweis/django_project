import re
from django.shortcuts import render , redirect
from .forms import UserregisterForm
from user import forms
from django.contrib import messages
def profile(request):
    return render(request,"user/profile.html")

def register(request):
    if request.method == 'POST':
        form = UserregisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request , f' مرحباً {username} تم أنشاء الحساب بنجاح  ')
            return redirect('home')
    else:
        form = UserregisterForm()
    context = {
        'title':'انشاء حساب جديد',
        'form':UserregisterForm()   
    }
    return render(request,"user/signUp.html",context)