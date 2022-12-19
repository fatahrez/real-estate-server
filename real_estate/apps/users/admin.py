from django.contrib import admin

import real_estate.apps.users.models as user_models

# Register your models here.
admin.site.register(user_models.User)