# Generated by Django 3.1.3 on 2020-12-01 13:23

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('merchan', '0012_auto_20201201_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='merchandise',
            name='likes',
            field=models.ManyToManyField(blank=True, null=True, related_name='like_list', to=settings.AUTH_USER_MODEL),
        ),
    ]