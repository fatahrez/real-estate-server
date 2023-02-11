# Generated by Django 4.1.4 on 2023-02-11 04:55

import autoslug.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("properties", "0002_alter_property_price"),
    ]

    operations = [
        migrations.CreateModel(
            name="NewProject",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True, null=True)),
                ("updated_at", models.DateTimeField(auto_now=True, null=True)),
                (
                    "deleted",
                    models.BooleanField(
                        default=False, help_text="This is for soft delete", null=True
                    ),
                ),
                ("is_active", models.BooleanField(default=True, null=True)),
                ("name", models.CharField(max_length=255)),
                (
                    "slug",
                    autoslug.fields.AutoSlugField(
                        always_update=True,
                        editable=False,
                        populate_from="title",
                        unique=True,
                    ),
                ),
                ("location", models.CharField(max_length=255)),
                (
                    "ref_code",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        unique=True,
                        verbose_name="New Project Reference Code",
                    ),
                ),
                ("description", models.TextField()),
                ("price", models.DecimalField(decimal_places=2, max_digits=12)),
                ("bedrooms", models.PositiveIntegerField()),
                ("bathrooms", models.PositiveIntegerField()),
                ("square_feet", models.PositiveIntegerField()),
                ("is_published", models.BooleanField(default=True)),
                (
                    "country",
                    django_countries.fields.CountryField(
                        default="KE", max_length=2, verbose_name="Country"
                    ),
                ),
                (
                    "city",
                    models.CharField(
                        default="Nairobi", max_length=180, verbose_name="City"
                    ),
                ),
                (
                    "construction_status",
                    models.CharField(
                        choices=[
                            ("Not Started", "Not Started"),
                            ("Under Construction", "Under Construction"),
                            ("Completed", "Completed"),
                        ],
                        default="Not Started",
                        max_length=255,
                    ),
                ),
                ("completion_date", models.DateField(blank=True, null=True)),
                (
                    "property_type",
                    models.CharField(
                        choices=[
                            ("House", "House"),
                            ("Apartment", "Apartment"),
                            ("Office", "Office"),
                            ("Commercial", "Commercial"),
                            ("Other", "Other"),
                        ],
                        default="Other",
                        max_length=50,
                        verbose_name="Property Type",
                    ),
                ),
                (
                    "cover_photo",
                    models.ImageField(
                        blank=True,
                        default="/house_sample.jpg",
                        null=True,
                        upload_to="",
                        verbose_name="Main Photo",
                    ),
                ),
                (
                    "photo1",
                    models.ImageField(
                        blank=True,
                        default="/interior_sample.jpg",
                        null=True,
                        upload_to="",
                    ),
                ),
                (
                    "photo2",
                    models.ImageField(
                        blank=True,
                        default="/interior_sample.jpg",
                        null=True,
                        upload_to="",
                    ),
                ),
                ("views", models.IntegerField(default=0, verbose_name="Total Views")),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="project_builder",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Agent, Seller, Buyer or Project Builder",
                    ),
                ),
            ],
            options={
                "ordering": ["-updated_at", "-created_at"],
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="NewProjectViews",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True, null=True)),
                ("updated_at", models.DateTimeField(auto_now=True, null=True)),
                (
                    "deleted",
                    models.BooleanField(
                        default=False, help_text="This is for soft delete", null=True
                    ),
                ),
                ("is_active", models.BooleanField(default=True, null=True)),
                ("ip", models.CharField(max_length=250, verbose_name="IP Address")),
                (
                    "new_project",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="new_project_views",
                        to="properties.newproject",
                    ),
                ),
            ],
            options={
                "verbose_name": "Total Views on New Project",
                "verbose_name_plural": "Total New Project Views",
            },
            managers=[
                ("everything", django.db.models.manager.Manager()),
            ],
        ),
    ]
