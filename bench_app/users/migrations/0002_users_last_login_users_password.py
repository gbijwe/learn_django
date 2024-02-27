# Generated by Django 5.0.2 on 2024-02-25 09:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="users",
            name="last_login",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="last login"
            ),
        ),
        migrations.AddField(
            model_name="users",
            name="password",
            field=models.CharField(
                default="pswd", max_length=128, verbose_name="password"
            ),
            preserve_default=False,
        ),
    ]
