# Generated by Django 4.2.10 on 2024-03-11 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_newslettersignup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newslettersignup',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
