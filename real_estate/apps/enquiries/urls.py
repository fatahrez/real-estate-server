from django.urls import path

from . import views

urlpatterns = [
    path("enquiry/all/", views.ListAllEnquiryAPIView.as_view(), name="all-enquries"),
    path("enquiry/details/<int:id>/", views.EnquiryDetailView.as_view(), name="enquiry-details"),
    path("enquiry/create/", views.send_enquiry_email, name="send-enquiry"),
]
