# Generated by Django 3.1.3 on 2020-11-21 12:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('merchan', '0002_auto_20201118_1922'),
    ]

    operations = [
        migrations.RenameField(
            model_name='merchandise',
            old_name='group',
            new_name='product',
        ),
        migrations.RemoveField(
            model_name='merchandise',
            name='age',
        ),
        migrations.RemoveField(
            model_name='merchandise',
            name='gender',
        ),
    ]