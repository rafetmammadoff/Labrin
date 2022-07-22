from django.apps import AppConfig


class CrmstudentConfig(AppConfig):
    name = 'crmstudent'

    def ready(self):
        import crmstudent.signals
        # import partners.tasks
