
from pyexpat import model
from django.shortcuts import render,redirect

from django.contrib import messages
from .forms import createUser

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
        'title':'أنشاء حساب جديد',
        'form':form,
    })