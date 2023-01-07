from django.db import models
from django.utils.translation import gettext_lazy as _
from real_estate.config.settings.base import AUTH_USER_MODEL
from real_estate.apps.users.models import Agent, Seller
from real_estate.apps.common.models import CommonFieldsMixin
from real_estate.apps.profiles.models import Profile

# Create your models here.
class Rating(models.Model):
    class Range(models.IntegerChoices):
        RATING_1 = 1, _("Poor")
        RATING_2 = 2, _("Fair")
        RATING_3 = 3, _("Good")
        RATING_4 = 4, _("Very Good")
        RATING_5 = 5, _("Excellent")

    rater = models.ForeignKey(AUTH_USER_MODEL, verbose_name=_("User Providing the rating"), on_delete=models.SET_NULL, null=True)
    agent = models.ForeignKey(
        Profile, 
        verbose_name=_("Agent being rated"), 
        on_delete=models.SET_NULL, 
        related_name="agent_review",
        null=True)
    rating = models.IntegerField(verbose_name=_("Rating"), choices=Range.choices, help_text="1=Poor, 2=Fair, 3=Good, 4=Very Good, 5=Excellent",
        default=0)
    comment = models.TextField(verbose_name=_("Comment"))

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        unique_together = ["rater", "agent"]
    
    def __str__(self):
        return f"{self.agent} rated at {self.rating}"
    


