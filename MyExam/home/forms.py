
from django import forms
import re
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from    .models import Question
class RegistrationForm(forms.Form):
    username = forms.CharField(label='Tài khoản', max_length=30)
    email = forms.EmailField(label='Email')
    first_name = forms.CharField(label='first name', max_length=30)
    last_name = forms.CharField(label='last name', max_length=150)
    password1 = forms.CharField(label='Mật khẩu', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Nhập lại mật khẩu', widget=forms.PasswordInput())

    def clean_password2(self):
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1 == password2 and password1:
                return password2
        raise forms.ValidationError("Mật khẩu không hợp lệ")
    def clean_username(self):
            username = self.cleaned_data['username']
            if not re.search(r'^\w+$', username):
                raise forms.ValidationError("Tên có kí tự đặc biệt")
            try:
                User.objects.get(username=username)
            except ObjectDoesNotExist:
                return username
            raise forms.ValidationError("Tài khoản đã tồn tại")
    def save(self):
            User.objects.create_user(username=self.cleaned_data['username'], email=self.cleaned_data['email'], first_name=self.cleaned_data['first_name'], last_name=self.cleaned_data['last_name'], password=self.cleaned_data['password1'])
    

class ChangePassword(forms.Form):
    old_password=forms.CharField(label='Nhập mật khẩu', widget=forms.PasswordInput())
    new_password=forms.CharField(label='Nhập mật khẩu mới', widget=forms.PasswordInput())
    reenter_password=forms.CharField(label='Nhập lại mật khẩu mới', widget=forms.PasswordInput())
    def clean(self):
        new_password=self.cleaned_data.get('new_password')
        reenter_password=self.cleaned_data.get('reenter_password')
        old_password=self.cleaned_data.get('old_password')
          #similarly old_password
        if new_password and new_password!=reenter_password or new_password == old_password:
            raise forms.ValidationError("Nhập lại mật khẩu!")
         #get the user object and check from old_password list if any one matches with the new password raise error(read whole answer you would know) 
        return self.cleaned_data #don't forget this.

