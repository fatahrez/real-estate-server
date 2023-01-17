from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "real_estate.apps.profiles"

    def ready(self):
        from real_estate.apps.profiles import signals