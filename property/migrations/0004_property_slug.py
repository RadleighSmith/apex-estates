# Generated by Django 4.2.10 on 2024-02-20 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_alter_property_options_property_title_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
