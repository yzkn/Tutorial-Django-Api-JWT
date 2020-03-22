from django.apps import AppConfig
from django.db.models.signals import post_migrate


class MyappConfig(AppConfig):
    name = 'myapp'

    def ready(self):
        from .models import create_default_item, create_default_subitem, create_default_user
        post_migrate.connect(create_default_user, sender=self)

        post_migrate.connect(create_default_item, sender=self)
        post_migrate.connect(create_default_subitem, sender=self)
