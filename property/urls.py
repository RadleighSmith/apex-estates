from django.urls import path
from . import views

urlpatterns = [
    path('property_listings/', views.PropertyList.as_view(), name='property_listings'),
    path('properties/<slug:slug>/', views.PropertyDetail.as_view(), name='property_detail'),
    path('properties/<slug:slug>/favourite/', views.favourite_property, name='favourite_property'),
    path('create/', views.create_property, name='create_property'),
    path('property/<slug:slug>/edit/', views.edit_property, name='edit_property'),
    path('property/<slug:slug>/delete/', views.delete_property, name='delete_property'),
]