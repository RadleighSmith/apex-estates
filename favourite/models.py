from django.db import models
from django.contrib.auth.models import User
from property.models import Property

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'property')