from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "real_estate.apps.users"

    def ready(self):
        from real_estate.apps.users import models