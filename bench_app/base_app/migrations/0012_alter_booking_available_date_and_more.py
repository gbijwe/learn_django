# Generated by Django 5.0.2 on 2024-03-13 05:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("base_app", "0011_alter_booking_owner"),
    ]

    operations = [
        migrations.AlterField(
            model_name="booking",
            name="available_date",
            field=models.DateField(blank=True, default="2024-03-13", null=True),
        ),
        migrations.AlterField(
            model_name="booking",
            name="booking_date",
            field=models.DateField(blank=True, default="2024-03-13", null=True),
        ),
        migrations.AlterField(
            model_name="resource",
            name="available_date",
            field=models.DateField(default="2024-03-13", null=True),
        ),
    ]
