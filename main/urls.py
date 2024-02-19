from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about_us/', views.about, name='about_us'),
    path('contact_us/', views.contact, name='contact_us'),
]