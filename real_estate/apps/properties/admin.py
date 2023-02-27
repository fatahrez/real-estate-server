from django.contrib import admin

from .models import Property, PropertyListingViews, PropertyViews, NewProject, NewProjectViews, PropertyListing


class PropertyAdmin(admin.ModelAdmin):
    list_display = ["title", "country", "advert_type", "property_type"]
    list_filter = ["advert_type", "property_type", "country"]


class NewProjectAdmin(admin.ModelAdmin):
    list_display = ["name", "country", "completion_date", "property_type"]
    list_filter = ["property_type", "completion_date", "country"]

admin.site.register(Property, PropertyAdmin)
admin.site.register(PropertyViews)
admin.site.register(NewProject, NewProjectAdmin)
admin.site.register(NewProjectViews)
admin.site.register(PropertyListing)
admin.site.register(PropertyListingViews)