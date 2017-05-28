from django.contrib.auth.models import User
from django import forms
from django.http import HttpResponse


class UserForm(forms.ModelForm):
    password1=forms.CharField(widget=forms.PasswordInput)
    password2=forms.CharField(label='passwword(again)',widget=forms.PasswordInput())
    class Meta:
        model=User
        fields=['username','email','password1','password2']


    def clean_password2(self):
        error_messages={
            'password_mismatch':('the two password field does not mathc.'),
        }

        if 'password1' in self.cleaned_data:
            password1=self.cleaned_data['password1']
            password2=self.cleaned_data['password2']
            if password1==password2:
                return password2
            else:
                return HttpResponse("password didint match")
