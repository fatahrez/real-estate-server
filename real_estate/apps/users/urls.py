from django.urls import path

from .views import (LoginAPIView, RegistrationAPIView)

app_name = 'users'
urlpatterns = [
    path('users/', RegistrationAPIView.as_view(), name='register_user'),
    path('users/login/', LoginAPIView.as_view(), name='login-user'),
]