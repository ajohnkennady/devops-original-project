# Generated by Django 4.1.5 on 2023-10-26 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="confirmrequest",
            name="accept",
            field=models.BooleanField(null=True),
        ),
    ]
