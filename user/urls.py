from atexit import register
from unicodedata import name
from django.urls import path
from. import views


urlpatterns= [
    path('',views.profile,name='profile'),
    path('signUp/',views.register,name='signUp')
]