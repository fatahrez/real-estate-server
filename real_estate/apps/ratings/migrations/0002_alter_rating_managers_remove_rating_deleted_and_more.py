# Generated by Django 4.1.4 on 2023-01-07 07:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("ratings", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="rating",
            managers=[],
        ),
        migrations.RemoveField(
            model_name="rating",
            name="deleted",
        ),
        migrations.RemoveField(
            model_name="rating",
            name="is_active",
        ),
    ]