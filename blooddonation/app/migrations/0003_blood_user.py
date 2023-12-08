# Generated by Django 4.1.5 on 2023-10-26 08:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0002_alter_confirmrequest_accept"),
    ]

    operations = [
        migrations.AddField(
            model_name="blood",
            name="user",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]