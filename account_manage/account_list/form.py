from django import forms

class Register_form(forms.Form):
    username = forms.CharField(required=True,min_length=3,max_length=15,error_messages={
        'min_length':'用户名长度不能低于3',
        'max_length':'用户名长度不能大于15',
        'require':'用户名不能为空',
    })
    password = forms.CharField(min_length=6,required=True,error_messages={
        'min_length':'密码长度不能低于6',
        'require':'密码不能为空',
    })


class Login_form(forms.Form):
    username = forms.CharField(required=True,min_length=3,max_length=15,error_messages={
        'min_length':'用户名长度不能低于3',
        'max_length':'用户名长度不能大于15',
        'require':'用户名不能为空',
    })
    password = forms.CharField(min_length=6,max_length=30,required=True,error_messages={
        'min_length':'密码长度不能低于6',
        'require':'密码不能为空',
    })