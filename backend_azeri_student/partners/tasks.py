# from __future__ import absolute_import, unicode_literals
import base64
from celery import shared_task
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
import sendgrid
import os
from sendgrid.helpers.mail import *
from django.conf import settings
from xhtml2pdf import pisa

# Use celery shared_task documentation here
# http://docs.celeryproject.org/en/latest/faq.html
from email_system.models import EmailTemplate
from partners.models import CitiesTables, EmailList


@shared_task()
def get_auto_reply(id, first, last, email, date_time, billing, number, base_id):
    if id:
        cities = CitiesTables.objects.filter(fk__id=id, cities__isnull=False)
        value = ' and '
        result = value.join([count.cities.name + ' (' + str(count.table_count) + ') ' for count in cities])
        table_count = sum([count.table_count for count in cities])
        full_name = first + " " + last
        file_creator.delay(id, date_time, table_count, email, full_name, billing, number, result, base_id)
        return "Successfuly done"
    else:
        print("No")
        return False


# Utility function
def convertHtmlToPdf(sourceHtml, outputFilename):
    # open output file for writing (truncated binary)
    resultFile = open(outputFilename, "w+b")

    # convert HTML to PDF
    pisaStatus = pisa.CreatePDF(
        sourceHtml,  # the HTML to convert
        dest=resultFile)  # file handle to recieve result

    # close output file
    resultFile.close()  # close output file

    # return True on success and False on errors
    return pisaStatus.err


@shared_task()
def file_creator(id, time, sum, email, full_name, billing_address, invoice_number, c_data, base_id):
    if base_id == 5:
        msg = EmailTemplate.objects.filter(id=5).last()
    else:
        msg = EmailTemplate.objects.filter(id=4).last()
    data = {
        'invoice_number': invoice_number,
        'bill_to': billing_address,
        'created_at': time,
        'total_count': sum,
        'total_price': int(sum) * 1550,
        'cities_data': c_data
    }
    convert_data = msg.context.format(**data)
    invoice_path = os.path.join(settings.MEDIA_ROOT, 'files')
    if not os.path.isdir(invoice_path):
        os.mkdir(invoice_path)
    file_name = os.path.join(invoice_path, 'out_{}.pdf'.format(id))
    pisa.showLogging()
    convertHtmlToPdf(convert_data, file_name)
    if base_id == 5:
        subject_text = "Registration for Fall fair 2019"
    else:
        subject_text = "Registration for Spring fair 2019"
    datas = {
        'subject': subject_text,
        'message': "Dear " + full_name + ". <br>Your invoice attached.",
        'file-name': file_name
    }
    get_send_reply_sms.delay(email, datas)
    return "Succesful create file"


@shared_task
def get_send_reply_sms(email, data):
    subject = data.get("subject")
    sg = sendgrid.SendGridAPIClient(apikey=settings.SENDGRID_API_KEY)
    from_email = Email("Azeristudent.az <info@azeristudent.az>")
    # p = Personalization()
    to_email = Email(email)
    content = Content("text/html", data.get("message"))
    mail = Mail(from_email, subject, to_email, content)
    # email_data = EmailList.objects.all()
    # if email_data:
    #     for e_date in email_data:
    #         p.add_cc(Email(e_date.email))
    pdf_path = data.get("file-name")
    with open(pdf_path, 'rb') as f:
        data_file = f.read()
    # Encode contents of file as Base 64
    encoded = base64.b64encode(data_file).decode()
    attachment = Attachment()
    attachment.content = encoded
    attachment.type = "application/pdf"
    attachment.filename = "invoice.pdf"
    attachment.disposition = "attachment"
    attachment.content_id = "PDF Document file"
    mail.add_attachment(attachment)
    # mail.add_personalization(p)
    response = sg.client.mail.send.post(request_body=mail.get())
    code = response.status_code
    if code == 202:
        get_send_reply_sms_our.delay(email, data)
    return "Message successfuly send {} !".format(code)


@shared_task
def get_send_reply_sms_our(email, data):
    subject = data.get("subject")
    sg = sendgrid.SendGridAPIClient(apikey=settings.SENDGRID_API_KEY)
    from_email = Email("Azeristudent.az <info@azeristudent.az>")
    p = Personalization()
    # email_data = EmailList.objects.all()
    content = Content("text/html", "Registration email: " + str(email))
    mail = Mail(from_email, subject, [], content)
    email_data = EmailList.objects.all()
    if email_data:
        for e_date in email_data:
            p.add_to(Email(e_date.email))
    pdf_path = data.get("file-name")
    with open(pdf_path, 'rb') as f:
        data_file = f.read()
    # Encode contents of file as Base 64
    encoded = base64.b64encode(data_file).decode()
    attachment = Attachment()
    attachment.content = encoded
    attachment.type = "application/pdf"
    attachment.filename = "invoice.pdf"
    attachment.disposition = "attachment"
    attachment.content_id = "PDF Document file"
    mail.add_attachment(attachment)
    mail.add_personalization(p)
    response = sg.client.mail.send.post(request_body=mail.get())
    code = response.status_code
    if code == 202:
        delete_file.delay(data)
    return "Message successfuly send {} !".format(code)


@shared_task()
def delete_file(data):
    if os.path.exists(data.get("file-name")):
        os.remove(data.get("file-name"))
    else:
        print("The file does not exist")
    return "Successful delete"
