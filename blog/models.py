from django.db import models
from django.contrib.auth.models import User 
from datetime import datetime
class Post (models.Model):
    title  = models.CharField( max_length=100)
    content = models.TextField()
    post_date = models.DateTimeField(default=datetime.now)
    post_update = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)


    def __str__(self):
        return str(self.title)


    class Meta:
        ordering = ("-post_date", )