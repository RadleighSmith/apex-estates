from django.urls import path
from . import views

urlpatterns = [
    path('property_listings/', views.property_listings, name='property_listings'),
]