# Generated by Django 4.2.10 on 2024-03-07 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ValuationRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('contact_number', models.CharField(max_length=15)),
                ('property_address', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('property_type', models.CharField(choices=[('house', 'House'), ('apartment', 'Apartment'), ('land', 'Land'), ('commercial', 'Commercial Property'), ('other', 'Other')], max_length=20)),
            ],
        ),
    ]