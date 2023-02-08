from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, login
from django.shortcuts import redirect, render
from django.views.generic import CreateView
from django.urls import reverse_lazy

from .forms import *


class Reg(CreateView):
    form_class = RegForm
    success_url = reverse_lazy('sends:home_form')
    template_name = 'authh/usercreation_form.html'


    def form_valid(self, form):
        login(self.request, form.save())
        return redirect('sends:home_form')


class Login(LoginView):
    form_class = AuthenticationForm
    template_name = 'authh/login.html'


def logout_user(req):
    logout(req)
    return redirect('sends:home_form')


def index(request):
    return render(request, 'authh/user_index.html')
