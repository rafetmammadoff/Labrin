# from django.db.models.signals import post_save, pre_delete, pre_save
# from django.dispatch import receiver
# from django.utils.safestring import mark_safe
#
# from student.tasks import get_send_reply_sms
# from .models import AutoReplayMessage, StudentInformation, SpecificityStudentMessage
#
#
# def check_email(instance):
#     if instance.email:
#         return instance.email
#     else:
#         return instance.parent_student_information.email
#
#
# @receiver(post_save, sender=StudentInformation, dispatch_uid='get_auto_reply')
# def get_auto_reply(sender, **kwargs):
#     instance = kwargs.get('instance')
#     if instance.cache_status != instance.status:
#         msg = AutoReplayMessage.objects.filter(types=instance.status).last()
#         specificitymsg = SpecificityStudentMessage.objects.filter(student=instance, types=instance.status).last()
#
#         if specificitymsg:
#             data = {'content': str(mark_safe(specificitymsg.content)), 'subject': specificitymsg.subject}
#             get_send_reply_sms.delay(check_email(instance), data)
#         elif msg:
#             data = {'content': str(mark_safe(msg.content)), 'subject': msg.subject}
#             get_send_reply_sms.delay(check_email(instance), data)
#     else:
#         print("No")
#         return False