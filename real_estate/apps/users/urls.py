from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import (LoginAPIView, RegistrationAPIView,SendPasswordResetEmail, 
                    UserRetrieveUpdateAPIView, ResetPasswordView)

app_name = 'users'
urlpatterns = [
    path('users/', RegistrationAPIView.as_view(), name='register_user'),
    path('users/login/', LoginAPIView.as_view(), name='login-user'),
    path('user/', UserRetrieveUpdateAPIView.as_view(), name='retrieve-edit-user'),
    path('users/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('users/password/reset/', SendPasswordResetEmail.as_view(), name='send-passwordreset-email'),
    path('users/password/reset/<str:token>', ResetPasswordView.as_view(), name='reset-password'),
]