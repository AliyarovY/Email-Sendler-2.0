from django.core.mail import send_mail
from django.conf import settings
from sends.models import *
from loguru import logger
from datetime import datetime
from django.core.management import BaseCommand



logger.add('sendler.log',
           format="{time•:HH:mm:ss} {level} {message}",
           level='DEBUG',
           rotation='500 MB',
           compression='zip',
           colorize=True,
           )

class Command(BaseCommand):
    @logger.catch
    def mail_send(self):
        title, message, emails, nl_object = *ARGS
        status = True
        message_time = nl_object.letter_time

        try:
            send_mail(
                subject=title,
                message=message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=emails
            )
            logger.debug('NICE')
        except Exception:
            status = False
            logger.error('BAD')

        # create Try_Send object
        TRY = Try_Send(
            try_time=message_time,
            try_status=status,
            try_newsletter=nl_object
        )
        TRY.save()

        return