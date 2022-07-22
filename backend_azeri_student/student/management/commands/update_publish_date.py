from django.core.management import BaseCommand

from student.models import Education


class Command(BaseCommand):
    help = 'Update Education publish date to created date'

    def handle(self, *args, **kwargs):
        educations = Education.objects.all()
        for edu in educations:
            try:
                data = Education.objects.get(id=edu.id)
                data.publish_date = data.created_at
                data.save()
                self.stdout.write('Education with id "%s" updated publish date to created date.' % edu.id)
            except Education.DoesNotExist:
                self.stdout.write('Education  with id "%s" does not exist.' % edu.id)
