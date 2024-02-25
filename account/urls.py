from django.urls import path
from . import views

urlpatterns = [
    path('sign_up/', views.sign_up, name='sign_up'),
    path('dashboard/', views.user_dashboard, name='dashboard'),
]