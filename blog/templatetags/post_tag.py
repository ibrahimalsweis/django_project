from atexit import register
from multiprocessing import context
from tkinter.tix import Form
from django import template
from blog.models  import  Post



register = template.Library()
@register.inclusion_tag('latest_posts.html')
def latest_posts():
    context = {
        'l_posts': Post.objects.all()[0:5],
    }
    return context
