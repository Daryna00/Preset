# Generated by Django 3.1.3 on 2020-12-09 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merchan', '0031_auto_20201209_1949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='merchandise',
            name='height_field1',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='merchandise',
            name='height_field2',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='merchandise',
            name='width_field1',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='merchandise',
            name='width_field2',
            field=models.IntegerField(default=0),
        ),
    ]