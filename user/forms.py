from django import forms 
from django.contrib.auth.models import User

          
class UserregisterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for fieldname in ['username']:
            self.fields[fieldname].help_text = None
    password1 = forms.CharField(label='كلمة المرور',max_length=100,widget=forms.PasswordInput(attrs={'class':"form-control my-2"}),min_length=8)
    password2 = forms.CharField(label='تأكيد كلمة المرور',max_length=100,widget=forms.PasswordInput(attrs={'class':"form-control my-2"}),min_length=8)
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            # 'password'
        ]
        widgets ={
          'username':forms.TextInput(attrs={'class':"form-control my-2"}),
          'email':forms.TextInput(attrs={'class':"form-control my-2"}),
          'first_name':forms.TextInput(attrs={'class':"form-control my-2"}),
          'last_name':forms.TextInput(attrs={'class':"form-control my-2"}),
        }
    def check_password(self):
        dpass = self.cleaned_data
        if dpass['password1'] != dpass['password2']:
            raise forms.ValidationError('كلمة المرور غير متطابقة')
        return dpass['password2']


    def clean_username(self):
        cd = self.cleaned_data
        if User.objects.filter(username=cd['username']).exists():
            raise forms.ValidationError('يوجد مستخدم مسجل بهذا الاسم.')
        return cd['username']