from django.db import models
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField

from real_estate.apps.common.models import CommonFieldsMixin
from real_estate.apps.users.models import User


# Create your models here.
class Gender(models.TextChoices):
    MALE = "Male", _("Male")
    FEMALE = "Female", _("Female")
    OTHER = "Other", _("Other")

    
class Profile(CommonFieldsMixin):
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE, null=True)
    phone_number = PhoneNumberField(verbose_name=_("Phone Number"), max_length=30, default="+254745678910")
    about_me = models.TextField(verbose_name=_("About Me"), default="say something about yourself...")
    license = models.CharField(verbose_name=_("Real Estate license"), max_length=20, blank=True, null=True)
    profile_photo = models.ImageField(verbose_name=_("Profile Photo"), default="/profile_default.png")
    gender = models.CharField(verbose_name=_("Gender"), choices=Gender.choices, default=Gender.OTHER, max_length=20)
    country = CountryField(verbose_name=_("Country"), default="KE", blank=False, null=False)
    city = models.CharField(verbose_name=_("City"), max_length=180, default="Nairobi", blank=False, null=False)
    rating = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    num_reviews = models.IntegerField(verbose_name=_("Number of Reviews"), default=0, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.user.username}'s profile"

