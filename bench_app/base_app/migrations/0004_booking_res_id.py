# Generated by Django 5.0.2 on 2024-03-11 06:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("base_app", "0003_alter_booking_available_date_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="booking",
            name="res_id",
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]