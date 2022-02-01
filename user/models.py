
from django.db import models
from django.contrib.auth.models import User
class Profile(models.Model):
    image = models.ImageField(upload_to='images',default='user_defualt.png')
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    
    def __str__(self):
        return str(f'حساب {self.user.username}')