from django import forms
from django.contrib.auth.models import User
from .models import Master, Account

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(label='비밀번호',
                               widget=forms.PasswordInput)
    password2 = forms.CharField(label='비밀번호 확인',
                               widget=forms.PasswordInput)
    nickname = forms.CharField(label='닉네임')

    class Meta:
        model = User
        fields = ('username',)
        labels = {
            'username': '아이디',
        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("Passwords don\'t match.")
        return cd['password2']

class AddAccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('site', 'username', 'password')
        labels = {
            'site': '사이트',
            'username': '아이디',
            'password': '비밀번호',
        }
