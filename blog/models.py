from email.policy import default
from django.db import models
from django.contrib.auth.models import User 
from datetime import datetime


class Post (models.Model):
    title  = models.CharField( max_length=100)
    content = models.TextField()
    post_date = models.DateTimeField(default=datetime.now)
    post_update = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE,null=True)


    def __str__(self):
        return str(self.title)


    class Meta:
        ordering = ("-post_date", )










class Comment(models.Model):
    name = models.CharField(max_length=50,)
    content_comment = models.TextField(max_length=500 ,verbose_name="اكتب تعليق")
    comment_date = models.DateTimeField(default=datetime.now)
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')

    class Meta:
        ordering = ("-comment_date", )
    def __str__(self):
        return str(f'علق {self.name} على {self.post}')