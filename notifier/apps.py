from django.apps import AppConfig


class NotifierConfig(AppConfig):
    name = 'notifier'

    def ready(self):
        # use signals here. 
        super().ready()
