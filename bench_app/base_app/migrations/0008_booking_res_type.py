# Generated by Django 5.0.2 on 2024-03-12 05:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("base_app", "0007_alter_booking_available_date_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="booking",
            name="res_type",
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
