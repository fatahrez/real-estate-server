# Generated by Django 4.1.4 on 2023-01-12 06:27

from django.db import migrations, models
import django.db.models.manager
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Enquiry",
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
                ("name", models.CharField(max_length=100, verbose_name="Your Name")),
                (
                    "phone_number",
                    phonenumber_field.modelfields.PhoneNumberField(
                        default="+254712345678",
                        max_length=30,
                        region=None,
                        verbose_name="Phone Number",
                    ),
                ),
                ("email", models.EmailField(max_length=254, verbose_name="Email")),
                ("subject", models.CharField(max_length=100, verbose_name="Subject")),
                ("message", models.TextField(verbose_name="Message")),
            ],
            options={
                "verbose_name_plural": "Enquiries",
            },
            managers=[
                ("everything", django.db.models.manager.Manager()),
            ],
        ),
    ]
