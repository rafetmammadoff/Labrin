from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from django.utils import timezone
from django.utils.safestring import mark_safe

from student.tasks import get_send_reply_sms
from .options.tools import slugify

from .models import Blog, Country, TrainingProgram, Service,Videos, News, Review, EducationCategory, Education, Event, ContactUs, \
    AutoReplyEvent, Exhibitions, ReservationDate
from django.utils.translation import gettext_lazy as _


# example of signal
@receiver(post_save, sender=Country, dispatch_uid='create_new_slug')
def create_new_slug(sender, **kwargs):
    """
    create slug for country model
    :param sender:
    :param kwargs:
    :return:
    """
    country = kwargs.get('instance')
    if not country.slug:
        country.slug = slugify(country.name)
        country.save()
    else:
        pass


@receiver(post_save, sender=TrainingProgram, dispatch_uid='create_slug')
def create_slug(sender, **kwargs):
    """
    create slug for country model
    :param sender:
    :param kwargs:
    :return:
    """
    instance = kwargs.get('instance')
    if not instance.slug:
        instance.slug = slugify(instance.name)
        instance.save()
    else:
        pass


@receiver(post_save, sender=Service, dispatch_uid='service_create_slug')
def service_create_slug(sender, **kwargs):
    instance = kwargs.get('instance')
    if not instance.slug:
        instance.slug = slugify(instance.name)
        instance.save()
    else:
        if instance.cache_name != instance.name:
            instance.cache_name = instance.name
            instance.slug = slugify(instance.name)
            instance.save()
        else:
            pass


@receiver(post_save, sender=News, dispatch_uid='news_create_slug')
def news_create_slug(sender, **kwargs):
    instance = kwargs.get('instance')
    if not instance.slug:
        instance.slug = slugify(instance.title) + instance.created_at.strftime("-%d-%m-%Y")
        instance.save()
    else:
        if instance.cache_title != instance.title:
            instance.cache_title = instance.title
            instance.slug = slugify(instance.title) + instance.created_at.strftime("-%d-%m-%Y")
            instance.save()
        else:
            pass


@receiver(post_save, sender=Blog, dispatch_uid='blog_create_slug')
def blog_create_slug(sender, **kwargs):
    instance = kwargs.get('instance')
    if not instance.slug:
        instance.slug = slugify(instance.title) + instance.created_at.strftime("-%d-%m-%Y")
        instance.save()
    else:
        if instance.cache_title != instance.title:
            instance.cache_title = instance.title
            instance.slug = slugify(instance.title) + instance.created_at.strftime("-%d-%m-%Y")
            instance.save()
        else:
            pass

@receiver(post_save, sender=Videos, dispatch_uid='video_create_slug')
def video_create_slug(sender, **kwargs):
    instance = kwargs.get('instance')
    if not instance.slug:
        instance.slug = slugify(instance.title) + instance.created_at.strftime("-%d-%m-%Y")
        instance.save()
    else:
        if instance.cache_title != instance.title:
            instance.cache_title = instance.title
            instance.slug = slugify(instance.title) + instance.created_at.strftime("-%d-%m-%Y")
            instance.save()
        else:
            pass

@receiver(post_save, sender=Exhibitions, dispatch_uid='exhibitions_create_slug')
def exhibitions_create_slug(sender, **kwargs):
    instance = kwargs.get('instance')
    if not instance.slug:
        instance.slug = slugify(instance.title) + instance.created_at.strftime("-%d-%m-%Y")
        instance.save()
    else:
        if instance.cache_title != instance.title:
            instance.cache_title = instance.title
            instance.slug = slugify(instance.title) + instance.created_at.strftime("-%d-%m-%Y")
            instance.save()
        else:
            pass


@receiver(post_save, sender=Review, dispatch_uid='review_create_slug')
def review_create_slug(sender, **kwargs):
    instance = kwargs.get('instance')
    if not instance.slug:
        instance.slug = slugify(instance.name) + instance.created_at.strftime("-%d-%m-%Y")
        instance.save()
    else:
        if instance.cache_name != instance.name:
            instance.cache_name = instance.name
            instance.slug = slugify(instance.name) + instance.created_at.strftime("-%d-%m-%Y")
            instance.save()
        else:
            pass


@receiver(post_save, sender=EducationCategory, dispatch_uid='educationcategory_create_slug')
def educationcategory_create_slug(sender, **kwargs):
    instance = kwargs.get('instance')
    if not instance.slug:
        instance.slug = slugify(instance.name)
        instance.save()
    else:
        if instance.cache_name != instance.name:
            instance.cache_name = instance.name
            instance.slug = slugify(instance.name)
            instance.save()
        else:
            pass


@receiver(post_save, sender=Event, dispatch_uid='event_create_model')
def event_create_model(sender, **kwargs):
    instance = kwargs.get('instance')
    if not instance.slug:
        instance.slug = slugify(instance.name) + instance.created_at.strftime("-%d-%m-%Y")
        instance.save()
    else:
        if instance.cache_name != instance.name:
            instance.cache_name = instance.name
            instance.slug = slugify(instance.name) + instance.created_at.strftime("-%d-%m-%Y")
            instance.save()
        else:
            pass


@receiver(post_save, sender=Education, dispatch_uid='edu_create_slug')
def edu_create_slug(sender, **kwargs):
    instance = kwargs.get('instance')
    if not instance.slug:
        instance.slug = slugify(instance.title) + instance.created_at.strftime("-%d-%m-%Y")
        instance.save()
    else:
        if instance.cache_title != instance.title:
            instance.cache_title = instance.title
            instance.slug = slugify(instance.title) + instance.created_at.strftime("-%d-%m-%Y")
            instance.save()
        else:
            pass


@receiver(post_save, sender=ContactUs, dispatch_uid='get_auto_reply')
def get_auto_reply(sender, **kwargs):
    instance = kwargs.get('instance')
    created = kwargs.get('created')
    if created:
        if instance.reference_url:
            if '/events/' in instance.reference_url and len(instance.reference_url) > 10:
                event = instance.get_event()
                msg = AutoReplyEvent.objects.last()
                if msg and event:
                    data = {}
                    data['event_name'] = event.name
                    data['event_date'] = event.event_date.strftime("%d.%m.%Y")
                    data['event_time'] = timezone.localtime(event.event_date).strftime("%H:%M")
                    data['event_area'] = event.area
                    data['full_name'] = instance.full_name
                    data['content'] = str(mark_safe(msg.content))
                    data['subject'] = msg.subject
                    get_send_reply_sms.delay(instance.email, data)
    else:
        print("No")
        return False


@receiver(post_save, sender=ReservationDate, dispatch_uid='get_reservation_auto_reply')
def get_reservation_auto_reply(sender, **kwargs):
    instance = kwargs.get('instance')
    created = kwargs.get('created')
    if created:
        monthArray = ["Yanvar", "Fevral", "Mart", "Aprel", "May", "Iyun", "Iyul", "Avqust", "Sentyabr", "Oktyabr",
                      "Noyabr", "Dekabr"]
        month = instance.date.strftime("%m")
        day = instance.date.strftime("%d")
        data = {'subject': "Sizin görüş istəyin qəbul olundu!",
                'content': "Sizin görüş istəyin qəbul olundu. " + str(day) + " " + str(monthArray[int(int(month)-1)]) + instance.date.strftime(" %Y %H.%M") + "-da sizi gözləyirik."}
        get_send_reply_sms.delay(instance.fk.email, data)
        content = str(day) + " " + str(monthArray[int(int(month)-1)]) + instance.date.strftime(" %Y %H.%M") + " üçün "\
                  + instance.fk.full_name + " tərəfindən yeni görüş alındı.<br>Email: " + instance.fk.email + \
                  "<br>Phone: " + instance.fk.phone + "<br> https://azeristudent.az/labmin/student/contactus/" + str(instance.fk.id) + "/change/"
        data_our = {'subject': "Yeni görüş tələbiniz var!", 'content': content}
        get_send_reply_sms.delay('info@azeristudent.az', data_our)
        #
    else:
        print("No")
        return False
