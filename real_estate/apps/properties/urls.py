from django.urls import path

from . import views

urlpatterns = [
    path("properties/all/", views.ListAgentsPropertiesAPIView.as_view(), name="all-properties"),
    path("properties/agents/", views.ListAgentsPropertiesAPIView.as_view(), name="agent-properties"),
    path("properties/create/", views.create_property_api_view, name="property-create"),
    path("properties/details/<slug:slug>/", views.PropertyDetailView.as_view(), name="property-details"),
    path("properties/update/<slug:slug>/", views.update_property_api_view, name="update-property"),
    path("properties/delete/<slug:slug>/", views.delete_property_api_view, name="delete-property"),
    path("properties/search/", views.PropertySearchAPIView.as_view(), name="property-search"),
]