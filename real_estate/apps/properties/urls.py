from unicodedata import name
from django.urls import path

from . import views

urlpatterns = [
    path(
        "properties/all/",
        views.ListAllPropertiesAPIView.as_view(),
        name="all-properties",
    ),
    path(
        "properties/agents/",
        views.ListAgentsPropertiesAPIView.as_view(),
        name="agent-properties",
    ),
    path("properties/create/", views.create_property_api_view, name="property-create"),
    path(
        "propertylisting/create/", 
        views.create_property_listing_api_view,
        name="property-listing-create"
    ),
    path(
        "properties/details/<slug:slug>/",
        views.PropertyDetailView.as_view(),
        name="property-details",
    ),
    path(
        "properties/update/<slug:slug>/",
        views.update_property_api_view,
        name="update-property",
    ),
    path(
        "properties/delete/<slug:slug>/",
        views.delete_property_api_view,
        name="delete-property",
    ),
    path(
        "properties/search/",
        views.PropertySearchAPIView.as_view(),
        name="property-search",
    ),
    path(
        "properties/new_projects/all/",
        views.ListAllNewProjectsAPIView.as_view(),
        name="all-new-projects"
    ),
    path(
        "properties/new_projects/details/<slug:slug>/",
        views.NewProjectDetailView.as_view(),
        name="new-project-details"
    ),
    path(
        "properties/new_projects/update/<slug:slug>/",
        views.update_new_project_api_view,
        name="update-new-project",
    ),
    path(
        "properties/new_projects/delete/<slug:slug>/",
        views.delete_new_project_api_view,
        name="delete-new-project"
    ),
]
