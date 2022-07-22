from django.core.management.base import BaseCommand
import subprocess


class Command(BaseCommand):

    def handle(self, *args, **options):
        print("Starting to npm run dev...")
        subprocess.call("cd _frontend/dev/ && npm run dev", shell=True)
        print("Exited .")
