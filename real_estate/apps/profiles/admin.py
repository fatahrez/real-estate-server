from django.contrib import admin

from real_estate.apps.profiles.models import Profile

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["id", "pk", "user", "gender", "phone_number", "country", "city"]
    list_filter = ["gender", "country", "city"]
    list_display_links = ["id", "pk", "user"]

admin.site.register(Profile, ProfileAdmin)
