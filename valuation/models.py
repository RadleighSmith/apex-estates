from django.db import models

class ValuationRequest(models.Model):
    name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    property_address = models.CharField(max_length=255)
    email = models.EmailField()
    PROPERTY_TYPES = [
        ('house', 'House'),
        ('apartment', 'Apartment'),
        ('land', 'Land'),
        ('commercial', 'Commercial Property'),
        ('other', 'Other')
    ]
    property_type = models.CharField(max_length=20, choices=PROPERTY_TYPES)

    def __str__(self):
        return self.name