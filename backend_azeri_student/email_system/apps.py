from django.apps import AppConfig


class EmailSystemConfig(AppConfig):
    name = 'email_system'

    verbose_name = "Email System"

    def ready(self):
        import email_system.tasks
