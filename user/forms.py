

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class createUser(UserCreationForm):
    password1 = forms.CharField(label='كلملة المرور',widget=forms.PasswordInput(attrs={'class':'form-control my-2'}),min_length=8)
    password2 = forms.CharField(label='ـأكيد كلمة المرور ',widget=forms.PasswordInput(attrs={'class':'form-control my-2'}),min_length=8)
 
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
    

        )
        widgets = {

            'username':forms.TextInput(attrs={'class':"form-control my-2"}),
            'email':forms.EmailInput(attrs={'class':'form-control my-2'}),
            'first_name':forms.TextInput(attrs={'class':'form-control my-2'}),
            'last_name':forms.TextInput(attrs={'class':'form-control my-2'}),
            'password1' :forms.PasswordInput(attrs={'class':'form-control my-2'}),
            'password2' :forms.PasswordInput(attrs={'class':'form-control my-2'}),
        }

    def clean_password2(self):
        data = self.cleaned_data
        if data['password1'] != data['password2']:
            raise forms.ValidationError('كلمة المرور غير متطابقة')
        return data['password2']




    def clean_usernam(self):
        data = self.cleaned_data            
        if User.objects.filter(username = data['username']).exists():
            raise forms.ValidationError('أسم المستحدم موجود بالفعل')    
        return  data['username']    

    def clean_email(self):
        data = self.cleaned_data            
        if User.objects.filter(email = data['email']).exists():
            raise forms.ValidationError(' هاذا البريد الاكترني مستخدم بالفعل')
        return  data['email']    


    # def clean_email(self):
    #     data = self.cleaned_data['email']            
    #     if User.objects.filter(email = data).exists():
    #         raise forms.ValidationError(' هاذا البريد الاكترني مستخدم بالفعل')




