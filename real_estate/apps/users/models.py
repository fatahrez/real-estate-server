from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser, CommonFieldsMixin):
    """ Base class for all users """
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=True)