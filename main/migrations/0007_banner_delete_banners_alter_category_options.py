# Generated by Django 4.2.2 on 2023-07-04 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_rename_image_banners_img_rename_image_category_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='banner/')),
                ('alt_text', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name_plural': '1. Banners',
            },
        ),
        migrations.DeleteModel(
            name='Banners',
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': '2. Categories'},
        ),
    ]
