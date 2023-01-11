from django.contrib import admin

import real_estate.apps.users.models as user_models

# Register your models here.
admin.site.register(user_models.User)
admin.site.register(user_models.Individual)
admin.site.register(user_models.Seller)
admin.site.register(user_models.Agent)
admin.site.register(user_models.ProjectBuilder)
admin.site.register(user_models.StaffMember)