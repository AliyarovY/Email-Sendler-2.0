import re
import json
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import *
from .utils import *
from .models import *


class Home_Form(LoginRequiredMixin, CreateView):
    model = Form
    fields = '__all__'
    template_name = 'sends/home_form.html'
    success_url = reverse_lazy('sends:post_form')
    login_url = reverse_lazy('authh:index')

    def get_context_data(self, **kwargs):
        kwargs['count'] = Newsletter.objects.all().count()
        kwargs['active'] = Newsletter.objects.filter(letter_status='created').count()

        if 'form' not in kwargs:
            kwargs['form'] = self.get_form()
        return super().get_context_data(**kwargs)


def post_form(request):
    global ARGS
    user = Form.objects.all().order_by('id').last()
    mls = re.split(r'[ ,;]', user.mails)
    mls = [x for x in mls if x]
    user.mails = mls
    user.save()

    # Client add
    clients_id = []
    emails = []
    for mail in mls:
        if len((x := mail.split('@'))) != 2 or '.' not in mail:
            continue
        name = x[0]
        client = Client(client_name=name, client_mail=mail)
        client.save()
        clients_id.append(client.id)
        emails.append(mail)
    clients_id = json.dumps(clients_id)

    # Message add
    message = Message(msg_title=user.msg_title, msg_body=user.msg_body)
    message.save()

    # Newsletter add
    letter_time = user.letter_time
    letter_periood = user.letter_periood
    letter = Newsletter(
        letter_time=letter_time,
        letter_periood=letter_periood,
        letter_message=message,
        letter_clients=clients_id,
        letter_mails=json.dumps(emails),
        letter_user=request.user
    )
    letter.save()

    # Collection
    coll = Collection(coll_clients=clients_id, coll_message=message, coll_newsletter=letter)
    coll.save()

    # End
    ARGS = [message.msg_title, message.msg_body, emails, letter]
    cron_add(letter)
    return redirect('sends:home_form')
