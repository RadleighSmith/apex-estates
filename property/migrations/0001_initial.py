# Generated by Django 4.2.10 on 2024-02-15 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property_type', models.IntegerField(choices=[(0, 'Detached House'), (1, 'Semi-Detached House'), (2, 'Terraced House'), (3, 'Apartment'), (4, 'Flat'), (5, 'Studio Apartment'), (6, 'Penthouse'), (7, 'Townhouse')], default=0)),
                ('location', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('bedrooms', models.PositiveIntegerField(default=0)),
                ('bathrooms', models.PositiveIntegerField(default=0)),
                ('garage', models.BooleanField(default=False)),
                ('parking', models.BooleanField(default=False)),
                ('description', models.TextField()),
                ('listed_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]