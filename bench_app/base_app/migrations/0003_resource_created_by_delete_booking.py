# Generated by Django 5.0.2 on 2024-03-06 03:10

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("base_app", "0002_resource_booking"),
    ]

    operations = [
        migrations.AddField(
            model_name="resource",
            name="created_by",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.DeleteModel(
            name="Booking",
        ),
    ]
