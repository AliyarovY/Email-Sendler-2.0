from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User
from captcha.fields import CaptchaField
from django import forms


class RegForm(UserCreationForm):
    # captcha = CaptchaField()
    code = forms.CharField(max_length=4, required=False)


    class Meta:
        model = User
        fields = ['username']


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = '__all__'


class MailVerifyForm(forms.Form):
    email = forms.EmailField(max_length=255, required=False)

