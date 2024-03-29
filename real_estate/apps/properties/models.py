from operator import mod
import random
import string
from tabnanny import verbose

from django import views

from autoslug import AutoSlugField
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField

from real_estate.apps.common.models import CommonFieldsMixin
from real_estate.apps.users.models import Agent, Seller

User = get_user_model()


class PropertyPublishedManager(models.Manager):
    def get_queryset(self):
        return (
            super(PropertyPublishedManager, self)
            .get_queryset()
            .filter(deleted=False, is_active=True)
        )

class Property(CommonFieldsMixin):
    class AdvertType(models.TextChoices):
        FOR_SALE = "For Sale", _("For Sale")
        FOR_RENT = "For Rent", _("For Rent")

    class PropertyType(models.TextChoices):
        HOUSE = "House", _("House")
        APARTMENT = "Apartment", _("Apartment")
        OFFICE = "Office", _("Office")
        COMMERCIAL = "Commercial", _("Commercial")
        OTHER = "Other", _("Other")

    user = models.ForeignKey(
        User,
        verbose_name=_("Agent, Seller, Buyer or Project Builder"),
        related_name="agent_buyer",
        on_delete=models.DO_NOTHING,
    )
    title = models.CharField(verbose_name=_("Property Title"), max_length=258)
    slug = AutoSlugField(populate_from="title", unique=True, always_update=True)
    ref_code = models.CharField(
        verbose_name=_("Property Reference Code"),
        max_length=255,
        unique=True,
        blank=True,
    )
    description = models.TextField(
        verbose_name=_("Description"), default="Default description..."
    )
    country = CountryField(
        verbose_name=_("Country"),
        default="KE",
        blank_label="(select country)",
    )
    city = models.CharField(verbose_name=_("City"), max_length=180, default="Nairobi")
    postal_code = models.CharField(
        verbose_name=_("Postal Code"), max_length=100, default="141"
    )
    street_address = models.CharField(
        verbose_name=_("Street Address"), max_length=150, default="Parklands Avenue"
    )
    property_number = models.IntegerField(
        verbose_name=_("Property Number"),
        validators=[MinValueValidator(1)],
        default=112,
    )
    price = models.DecimalField(
        verbose_name=_("Price"), max_digits=10, decimal_places=2, default=0.0
    )
    plot_area = models.DecimalField(
        verbose_name=_("Plot Area(m^2)"), max_digits=8, decimal_places=2, default=0.0
    )
    total_floors = models.IntegerField(verbose_name=_("Number of floors"), default=0)
    bedrooms = models.IntegerField(verbose_name=_("Bedrooms"), default=1)
    bathrooms = models.DecimalField(
        verbose_name=_("Bathrooms"), max_digits=4, decimal_places=2, default=1.0
    )
    advert_type = models.CharField(
        verbose_name=_("Advert Type"),
        max_length=50,
        choices=AdvertType.choices,
        default=AdvertType.FOR_SALE,
    )
    property_type = models.CharField(
        verbose_name=_("Property Type"),
        max_length=50,
        choices=PropertyType.choices,
        default=PropertyType.OTHER,
    )
    cover_photo = models.ImageField(
        verbose_name=_("Main Photo"), default="/house_sample.jpg", null=True, blank=True
    )
    photo1 = models.ImageField(default="/interior_sample.jpg", null=True, blank=True)
    photo2 = models.ImageField(default="/interior_sample.jpg", null=True, blank=True)
    photo3 = models.ImageField(default="/interior_sample.jpg", null=True, blank=True)
    photo4 = models.ImageField(default="/interior_sample.jpg", null=True, blank=True)
    published_status = models.BooleanField(
        verbose_name=_("Published Status"), default=False
    )
    views = models.IntegerField(verbose_name=_("Total Views"), default=0)

    objects = models.Manager()
    published = PropertyPublishedManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Property"
        verbose_name_plural = "Properties"

    def save(self, *args, **kwargs):
        self.title = str.title(self.title)
        self.description = str.capitalize(self.description)
        self.ref_code = "".join(
            random.choices(string.ascii_uppercase + string.digits, k=10)
        )
        super(Property, self).save(*args, **kwargs)


class PropertyViews(CommonFieldsMixin):
    ip = models.CharField(verbose_name=_("IP Address"), max_length=250)
    property = models.ForeignKey(
        Property, related_name="Property", on_delete=models.CASCADE
    )

    def __str__(self):
        return (
            f"Total views on - {self.property.title} is - {self.property.views} view(s)"
        )

    class Meta:
        verbose_name = "Total Views on Property"
        verbose_name_plural = "Total Property Views"

class PropertyListing(CommonFieldsMixin):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    views = models.IntegerField(verbose_name=_("Total Views"), default=0)

    def save(self, *args, **kwargs):
        self.is_active = True
        super(PropertyListing, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.property} - {self.agent}"

class PropertyListingViews(CommonFieldsMixin):
    ip = models.CharField(verbose_name=_("IP Address"), max_length=250)
    property_listing = models.ForeignKey(
        PropertyListing, related_name="PropertyListing", on_delete=models.CASCADE
    )

    def __str__(self):
        return (
            f"Total views on - {self.property_listing} is - {self.property_listing.views} view(s)"
        )
    
    class Meta:
        verbose_name = "Total Views on Property Listing"
        verbose_name_plural = "Total Property Listing Views"


class NewProject(CommonFieldsMixin):

    class PropertyType(models.TextChoices):
        HOUSE = "House", _("House")
        APARTMENT = "Apartment", _("Apartment")
        OFFICE = "Office", _("Office")
        COMMERCIAL = "Commercial", _("Commercial")
        OTHER = "Other", _("Other")
    

    name = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from="name", unique=True, always_update=True)
    location = models.CharField(max_length=255)
    user = models.ForeignKey(
        User,
        verbose_name=_("Agent, Seller, Buyer or Project Builder"),
        related_name="project_builder",
        on_delete=models.DO_NOTHING,
    )
    ref_code = models.CharField(
        verbose_name=_("New Project Reference Code"),
        max_length=255,
        unique=True,
        blank=True,
    )
    description = models.TextField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    bedrooms = models.PositiveIntegerField()
    bathrooms = models.PositiveIntegerField()
    square_feet = models.PositiveIntegerField()
    is_published = models.BooleanField(default=True)
    country = CountryField(
        verbose_name=_("Country"),
        default="KE",
        blank_label="(select country)",
    )
    city = models.CharField(verbose_name=_("City"), max_length=180, default="Nairobi")
    construction_status = models.CharField(
        max_length=255,
        choices=(
            ('Not Started', 'Not Started'),
            ('Under Construction', 'Under Construction'),
            ('Completed', 'Completed'),
        ),
        default='Not Started'
    )
    completion_date = models.DateField(null=True, blank=True)
    property_type = models.CharField(
        verbose_name=_("Property Type"),
        max_length=50,
        choices=PropertyType.choices,
        default=PropertyType.OTHER,
    )
    published_status = models.BooleanField(
        verbose_name=_("Published Status"), default=False
    )
    cover_photo = models.ImageField(
        verbose_name=_("Main Photo"), default="/house_sample.jpg", null=True, blank=True
    )
    photo1 = models.ImageField(default="/interior_sample.jpg", null=True, blank=True)
    photo2 = models.ImageField(default="/interior_sample.jpg", null=True, blank=True)
    views = models.IntegerField(verbose_name=_("Total Views"), default=0)

    
    objects = models.Manager()
    published = PropertyPublishedManager()

    def save(self, *args, **kwargs):
        self.name = str.title(self.name)
        self.description = str.capitalize(self.description)
        self.ref_code = "".join(
            random.choices(string.ascii_uppercase + string.digits, k=10)
        )
        super(NewProject, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class NewProjectViews(CommonFieldsMixin):
    ip = models.CharField(verbose_name=_("IP Address"), max_length=250)
    new_project = models.ForeignKey(
        NewProject, related_name="NewProject", on_delete=models.CASCADE
    )

    def __str__(self):
        return (
            f"Total views on - {self.new_project.name} is - {self.new_project.views} view(s)"
        )

    class Meta:
        verbose_name = "Total Views on New Project"
        verbose_name_plural = "Total New Project Views"
