from django.urls import path
from . import views

urlpatterns = [
    path('sign_up/', views.sign_up, name='sign_up'),
    path('dashboard/', views.user_dashboard, name='dashboard'),
    path('delete/message/<int:message_id>/', views.delete_message, name='delete_message'),
    path('delete/valuation/<int:valuation_id>/', views.delete_valuation, name='delete_valuation'),
]