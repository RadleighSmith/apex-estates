# Generated by Django 4.2.10 on 2024-03-08 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0008_alter_property_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, unique=True),
        ),
    ]