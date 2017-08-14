from django import forms
from django.contrib.auth.models import User
from .models import Master

class MasterRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='비밀번호',
                               widget=forms.PasswordInput)
    password2 = forms.CharField(label='비밀번호 확인',
                               widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('username',)

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("Passwords don\'t match.")
        return cd['password2']
