# Generated by Django 3.1.3 on 2020-12-02 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merchan', '0017_auto_20201202_1451'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='merchandise',
            name='height_field',
        ),
        migrations.RemoveField(
            model_name='merchandise',
            name='width_field',
        ),
        migrations.AlterField(
            model_name='merchandise',
            name='after_img',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
