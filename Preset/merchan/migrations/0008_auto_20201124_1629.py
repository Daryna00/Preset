# Generated by Django 3.1.3 on 2020-11-24 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merchan', '0007_auto_20201124_1435'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='merchandise',
            options={'ordering': ['-timestamp', '-updated']},
        ),
        migrations.RenameField(
            model_name='merchandise',
            old_name='img',
            new_name='after_img',
        ),
        migrations.AddField(
            model_name='merchandise',
            name='before_img',
            field=models.ImageField(blank=True, height_field='height_field', null=True, upload_to='images/', width_field='width_field'),
        ),
    ]
