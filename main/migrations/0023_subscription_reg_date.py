# Generated by Django 4.2.2 on 2023-07-15 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_subplan_validity_days'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='reg_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
