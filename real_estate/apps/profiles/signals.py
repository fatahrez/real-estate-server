import logging

from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Profile
from real_estate.apps.users.models import User
from real_estate.apps.users.models import StaffMember
from real_estate.apps.users.models import ProjectBuilder
from real_estate.apps.users.models import Agent
from real_estate.apps.users.models import Seller
from real_estate.apps.users.models import Individual

logger = logging.getLogger(__name__)

@receiver(post_save, sender=StaffMember)
@receiver(post_save, sender=ProjectBuilder)
@receiver(post_save, sender=Agent)
@receiver(post_save, sender=Seller)
@receiver(post_save, sender=Individual)
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=StaffMember)
@receiver(post_save, sender=ProjectBuilder)
@receiver(post_save, sender=Agent)
@receiver(post_save, sender=Seller)
@receiver(post_save, sender=Individual)
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, **kwargs):
    try:
        instance.profile
    except Profile.DoesNotExist:
        Profile.objects.create(user=instance)
    instance.profile.save()
    logger.info(f"{instance}'s profile created")
