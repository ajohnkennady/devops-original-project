# Generated by Django 4.2.4 on 2023-10-27 05:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_delete_blood'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospital',
            name='hospitalname',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.CreateModel(
            name='Blood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bloodgroupname', models.CharField(choices=[('A+', 'a+'), ('A-', 'a-'), ('B-', 'b-'), ('B+', 'b+'), ('O+', 'o+'), ('O-', 'o-'), ('AB+', 'ab+'), ('AB-', 'ab-')], max_length=5)),
                ('loaction', models.TextField()),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
