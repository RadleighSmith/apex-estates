from django.db import models
from django.contrib.auth.models import User

STRUCTURE_CATEGORY = (
    (0, "Detached House"),
    (1, "Semi-Detached House"),
    (2, "Terraced House"),
    (3, "Apartment"),
    (4, "Flat"),
    (5, "Studio Apartment"),
    (6, "Penthouse"),
    (7, "Townhouse"),
)

class Property(models.Model):
    property_type = models.IntegerField(choices=STRUCTURE_CATEGORY, default=0)
    location = models.CharField(max_length=100)
    price = models.IntegerField()
    bedrooms = models.PositiveIntegerField(default=0)
    bathrooms = models.PositiveIntegerField(default=0)
    garage = models.BooleanField(default=False)
    parking = models.BooleanField(default=False)
    description = models.TextField()
    listed_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)