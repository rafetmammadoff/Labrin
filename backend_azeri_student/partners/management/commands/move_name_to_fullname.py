from django.core.management import BaseCommand

from partners.models import RegisterFair


class Command(BaseCommand):
    help = 'Move first and last name to full name'

    def handle(self, *args, **kwargs):
        registered_people = RegisterFair.objects.all()
        for person in registered_people:
            try:
                data = RegisterFair.objects.get(id=person.id)
                data.full_name = data.first_name + " " + data.last_name
                data.save()
                self.stdout.write('Education with id "%s" saved full_name' % person.id)
            except RegisterFair.DoesNotExist:
                self.stdout.write('RegisterFair  with id "%s" does not exist.' % person.id)
