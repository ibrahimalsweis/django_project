
from django import forms
from .models import Comment

class commentsForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content_comment']

        widgets ={
            'content_comment':forms.TextInput(attrs={'class':"form-control my-2"})
        }