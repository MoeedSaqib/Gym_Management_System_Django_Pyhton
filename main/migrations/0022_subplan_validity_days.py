# Generated by Django 4.2.2 on 2023-07-15 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_remove_assignsubscriber_subscriber_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='subplan',
            name='validity_days',
            field=models.IntegerField(null=True),
        ),
    ]
