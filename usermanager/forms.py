from . import models
# from django.forms import forms, fields
from django import forms


class UserCheck(forms.Form):
    username = forms.CharField(required=True, max_length=16, min_length=4, error_messages={
        'required': "用户名不能为空",
        'max_length': "长度太长",
        "min_length": "长度太短",

    }, widget=forms.TextInput(attrs={'class': 'form-control'})
                               )
    password = forms.CharField(required=True, max_length=16, min_length=3, error_messages={
        'required': "密码不能为空",
        'max_length': "长度太长",
        "min_length": "长度太短",

    }, widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    email = forms.EmailField()


class UserLoginCheck(forms.Form):
    username = forms.CharField(required=True, max_length=16, min_length=4, error_messages={
        'required': "用户名不能为空",
        'max_length': "长度太长",
        "min_length": "长度太短",

    }, widget=forms.TextInput(attrs={'class': 'form-control'})
                               )
    password = forms.CharField(required=True, max_length=16, min_length=3, error_messages={
        'required': "密码不能为空",
        'max_length': "长度太长",
        "min_length": "长度太短",

    }, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
