from django.apps import AppConfig


class IbalertConfig(AppConfig):
    name = "ibalert"

    def ready(self):
        # use signals here.
        super().ready()
