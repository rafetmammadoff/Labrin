# from __future__ import absolute_import, unicode_literals
from celery import shared_task
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
import sendgrid
import os
from sendgrid.helpers.mail import *


# Use celery shared_task documentation here
# http://docs.celeryproject.org/en/latest/faq.html


@shared_task
def get_send_reply_sms(email, data):
    subject = data.get("subject")
    sg = sendgrid.SendGridAPIClient(apikey=settings.SENDGRID_API_KEY)
    from_email = Email("Azeristudent.az <info@azeristudent.az>")
    to_email = Email(email)
    content = Content("text/html", data.get("content").format(**data))
    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    code = response.status_code
    return "Message successfuly send {} !".format(code)
