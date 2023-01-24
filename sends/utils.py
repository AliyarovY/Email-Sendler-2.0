import subprocess

from django.core.mail import send_mail
from django.conf import settings
from .models import Try_Send, WEEK, DAY, MONTH
from datetime import datetime


def cron_add(nl_object):
    result = ['*'] * 5

    time = nl_object.letter_time
    result[:2] = str(time).split(':')[:2]

    dt = datetime.now()
    periood = nl_object.letter_periood
    if periood == MONTH:
        result[-2] = '/' + dt.month
    elif periood == WEEK:
        result[~0] = '/' + dt.isoweekday()

    result = (' '.join(result), 'django.core.management.mail_send', ['command'])
    settings.CRONJOBS.append(result)

    x = subprocess.run(
    'python3 manage.py crontab add'.split(),
    stdout = subprocess.DEVNULL,
    stderr = subprocess.DEVNULL,
    encoding = 'utf-8'
    )

    return

