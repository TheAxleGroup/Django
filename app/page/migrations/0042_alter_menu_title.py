# Generated by Django 3.2.16 on 2023-02-20 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0041_auto_20230118_1318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='title',
            field=models.CharField(choices=[('main-header-menu', 'Main Header Menu'), ('main-eyebrow-menu', 'Main Eyebrow Menu'), ('footer-extra-menu', 'Footer Extra Menu')], max_length=30),
        ),
    ]
