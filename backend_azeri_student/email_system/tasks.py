from __future__ import absolute_import, unicode_literals
from celery import shared_task
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
import sendgrid
import os
from sendgrid.helpers.mail import *

# Use celery shared_task documentation here
# http://docs.celeryproject.org/en/latest/faq.html
from .models import EmailData, EmailHistory, EmailTemplate


@shared_task
def send_grid_bulk_email(id_list):
    sg = sendgrid.SendGridAPIClient(apikey=settings.SENDGRID_API_KEY)
    from_email = Email("Azeristudent.az <info@azeristudent.az>")
    all_emails = EmailData.objects.filter(id__in=id_list)
    template = EmailTemplate.objects.all().first()
    for email in all_emails:
        if not EmailHistory.objects.filter(email=email.email, template=template).exists():
            to_email = Email(email.email)
            e_history = EmailHistory()
            e_history.email = email.email
            e_history.template = template
            subject = template.name
            content = Content("text/html", template.context)
            mail = Mail(from_email, subject, to_email, content)
            response = sg.client.mail.send.post(request_body=mail.get())
            print(response.status_code)
            e_history.status = True if response.status_code == 202 else False
            e_history.save()
            # print(response.status_code)
            # print(response.headers)
    return "Message successfuly send !"


@shared_task
def test_celery():
    print("Yes it works")
    return "Done"
