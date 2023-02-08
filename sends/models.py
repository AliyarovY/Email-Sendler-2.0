from django.db.models import *
from django.contrib.auth.models import User
from django.urls import reverse


ARGS = []

NULLABLE = dict(blank=True, null=True)

CREATED = 'created'
COMPLATED = 'completed'
STARTED = 'started'

STATUS_CHOICES = [
    (CREATED, 'created'),
    (COMPLATED, 'completed'),
    (STARTED, 'started'),
]

MONTH = 'month'
WEEK = 'week'
DAY = 'day'

PERIOOD_CHOICES = [
    (DAY, 'day'),
    (WEEK, 'week'),
    (MONTH, 'month'),
]


class Client(Model):
    client_mail = EmailField(max_length=255)
    client_name = CharField(max_length=255)
    client_comm = TextField(**NULLABLE)


    def __str__(self):
        return self.client_name


class Newsletter(Model):
    letter_time = TimeField()
    letter_periood = CharField(max_length=10, choices=PERIOOD_CHOICES, default=DAY)
    letter_status = CharField(max_length=10, choices=STATUS_CHOICES, default=STARTED)
    letter_message = ForeignKey('Message', on_delete=SET_NULL, null=True)
    letter_clients = TextField(**NULLABLE)
    letter_mails = TextField(**NULLABLE)
    letter_user = ForeignKey(User, on_delete=CASCADE, null=True, default=None)


    def __str__(self):
        return str(self.letter_user) + ' : '+ str(self.letter_time)

    def get_url(self):
        return reverse('mailings:update', args=[self.id])

    def get_del_url(self):
        return reverse('mailings:delete', args=[self.id])

    def print_periood(self):
        return str(self.letter_periood)


class Message(Model):
    msg_title = CharField(max_length=255)
    msg_body = CharField(max_length=255)


    def __str__(self):
        return self.msg_title


class Try_Send(Model):
    try_time = DateTimeField(auto_now_add=True)
    try_status = BooleanField(default=True)
    try_reply = TextField(**NULLABLE)
    try_newsletter = ForeignKey('Newsletter', null=True, on_delete=SET_NULL)


class Form(Model):
    mails = TextField()

    letter_time = TimeField()
    letter_periood = CharField(max_length=10, choices=PERIOOD_CHOICES, default=DAY)

    msg_title = CharField(max_length=255, verbose_name='Message Title')
    msg_body = TextField(max_length=1000, verbose_name='Message Body')


class Collection(Model):
    coll_clients = TextField()
    coll_message = ForeignKey('Message', on_delete=SET_NULL, null=True)
    coll_newsletter = ForeignKey('Newsletter', on_delete=SET_NULL, null=True)
