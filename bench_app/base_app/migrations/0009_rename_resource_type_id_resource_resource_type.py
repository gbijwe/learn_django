# Generated by Django 5.0.2 on 2024-03-08 15:44

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("base_app", "0008_rename_resource_type_resource_resource_type_id"),
    ]

    operations = [
        migrations.RenameField(
            model_name="resource",
            old_name="resource_type_id",
            new_name="resource_type",
        ),
    ]
