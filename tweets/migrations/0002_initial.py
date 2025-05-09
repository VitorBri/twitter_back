# Generated by Django 4.2.20 on 2025-04-09 04:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("tweets", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="tweets",
            name="likes",
            field=models.ManyToManyField(
                blank=True, related_name="liked_tweets", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="tweets",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="tweets",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
