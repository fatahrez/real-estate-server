from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver

from rest_framework_simplejwt.tokens import RefreshToken

from real_estate.apps.common.models import CommonFieldsMixin
# Create your models here.
class User(AbstractUser, CommonFieldsMixin):
    """ Base class for all users """
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)

    class Types(models.TextChoices):
        """ User Types """
        INDIVIDUAL = "INDIVIDUAL", "Individual"
        SELLER = "SELLER", "Seller"
        AGENT = "AGENT", "Agent"
        PROJECTBUILDER = "PROJECTBUILDER", "ProjectBuilder"
        STAFFMEMBER = "STAFFMEMBER", "StaffMember"
        ADMIN = "ADMIN", "Admin"

    base_type = Types.ADMIN
    type = models.CharField(_("Type"), max_length=50, choices=Types.choices, default=base_type)
    email = models.CharField(_("email of User"), unique=True, max_length=255)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = self.base_type
            return super().save(*args, kwargs)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }


""" ========================= Proxy Model Managers =================== """


class IndividualManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.INDIVIDUAL)


class SellerManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.SELLER)


class AgentManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.AGENT)

class ProjectBuilderManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.PROJECTBUILDER)


class StaffManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.STAFFMEMBER)


""" ============================ Proxy Models ======================= """


class Individual(User):
    """Class to create Individual Object & Associated attributes """
    base_type = User.Types.INDIVIDUAL
    objects = IndividualManager()

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = User.Types.INDIVIDUAL
            self.set_password(self.password)
        return super().save(*args, **kwargs)

    class Meta:
        proxy = True
        ordering = ['-created_at', '-updated_at']


class Seller(User):
    """ class to create Seller object & associated attributes """
    base_type = User.Types.SELLER
    objects = SellerManager()

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = User.Types.SELLER
            self.set_password(self.password)
        return super().save(*args, **kwargs)

    class Meta:
        proxy = True
        ordering = ['-created_at', '-updated_at']


class Agent(User):
    """ Class to create Agent object & associated attributes """
    base_type = User.Types.AGENT
    objects = AgentManager()

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = User.Types.AGENT
            self.set_password(self.password)
        return super().save(*args, **kwargs)

    class Meta:
        proxy = True
        ordering = ['-created_at', '-updated_at']

class ProjectBuilder(User):
    """ Class to create ProjectBuilder & associated attributes """
    base_type = User.Types.PROJECTBUILDER
    objects = ProjectBuilderManager()

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = User.Types.PROJECTBUILDER
            self.set_password(self.password)
        return super().save(*args, **kwargs)

    class Meta:
        proxy = True
        ordering = ['-created_at', '-updated_at']


class StaffMember(User):
    """ Class to create StaffMember objects & associated attributes """
    base_type = User.Types.STAFFMEMBER
    objects = StaffManager()

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = User.Types.STAFFMEMBER
            self.set_password(self.password)
        return super().save(*args, **kwargs)

    class Meta:
        proxy = True
        ordering = ['-created_at', '-updated_at']


@receiver(post_save, sender=StaffMember)
@receiver(post_save, sender=ProjectBuilder)
@receiver(post_save, sender=Agent)
@receiver(post_save, sender=Seller)
@receiver(post_save, sender=Individual)
def create_user_profile(sender, instance, created, **kwargs):
    from real_estate.apps.profiles.models import Profile
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=StaffMember)
@receiver(post_save, sender=ProjectBuilder)
@receiver(post_save, sender=Agent)
@receiver(post_save, sender=Seller)
@receiver(post_save, sender=Individual)
def create_user_profile(sender, instance, **kwargs):
    instance.profile.save()    
