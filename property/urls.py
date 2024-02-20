from django.urls import path
from . import views

urlpatterns = [
    path('property_listings/', views.PropertyList.as_view(), name='property_listings'),
    path('<slug:slug>/', views.PropertyDetail.as_view(), name='property_detail'),
]