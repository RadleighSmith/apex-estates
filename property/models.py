from django.db import models
from django.contrib.auth.models import User

PROPERTY_TYPE_CHOICES= (
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
    title = models.CharField(default="Title", max_length=200)
    property_type = models.IntegerField(choices=PROPERTY_TYPE_CHOICES, default=0)
    location = models.CharField(max_length=100, unique=True)
    price = models.IntegerField()
    bedrooms = models.PositiveIntegerField(default=0)
    bathrooms = models.PositiveIntegerField(default=0)
    garage = models.BooleanField(default=False)
    parking = models.BooleanField(default=False)
    description = models.TextField()
    listed_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = "Properties"
        ordering = ["-listed_on"]
    
    def __str__(self):
        property_type_display = dict(PROPERTY_TYPE_CHOICES).get(self.property_type, 'Unknown Property Type')
        return f"{property_type_display} in {self.location}"