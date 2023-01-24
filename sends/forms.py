from django import forms as f
from .models import *


class HomeForm(f.Form):
    client_mail = f.EmailField(max_length=40)
    client_name = f.CharField(max_length=255)
    client_comm = f.CharField(max_length=1000)

    letter_time = TimeField()
    letter_period = f.CharField(max_length=10)
    letter_status = f.CharField(max_length=10)

    msg_title = f.CharField(max_length=255, label='Message Title')
    msg_body = f.CharField(max_length=1000, label='Message Body')
