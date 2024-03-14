from django.urls import path
from . import views


urlpatterns = [
    path('request_valuation/', views.valuation_request, name='valuation_request'),
]
