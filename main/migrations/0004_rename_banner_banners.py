# Generated by Django 4.2.2 on 2023-07-04 16:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_rename_banners_banner'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Banner',
            new_name='Banners',
        ),
    ]
