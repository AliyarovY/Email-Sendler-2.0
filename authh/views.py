from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, login
from django.shortcuts import redirect, render

from django.core.mail import send_mail
from django.conf import settings
from django.core.exceptions import ValidationError

from .models import User
from .forms import *
from .services import *

from random import randint


def link_func(req):
    global is_verify
    is_verify = True
    return redirect('authh:post_reg')


def email_verify(request):
    if request.method == 'POST':
        form = MailVerifyForm(request.POST)
        if form.is_valid():
            code = str(randint(1000, 9999))
            email = request.POST['email']
            set_email(email)
            set_code(code)

            send_mail(
                subject='Verify Code',
                message=f'{code}',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[email]
            )
            return redirect('authh:post_reg')
        else:
            ValidationError()
    else:
        form = MailVerifyForm()

    return render(request, 'authh/mailverify.html', {'form': form})


def reg(request):
    if request.method == 'POST':
        form = RegForm(request.POST)
        if form.is_valid():
            user_code = request.POST['code']
            code = get_code()
            email = get_email()
            if user_code == code:
                User(username=request.POST['username'], email=email)
                login(request, form.save())
                return redirect('sends:home_form')
            else:
                ValidationError('not verify')
    else:
        form = RegForm()
    return render(request, 'authh/usercreation_form.html', {'form': form})


class Login(LoginView):
    form_class = LoginForm
    template_name = 'authh/login.html'


def logout_user(req):
    logout(req)
    return redirect('sends:home_form')


def index(request):
    return render(request, 'authh/user_index.html')
