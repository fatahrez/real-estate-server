from django.urls import path

from . import views

urlpatterns = [path("enquiry", views.send_enquiry_email, name="send-enquiry")]
