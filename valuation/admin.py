from django.contrib import admin
from .models import ValuationRequest

@admin.register(ValuationRequest)
class ValuationRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_number', 'property_address', 'email', 'property_type')
    search_fields = ('name', 'contact_number', 'property_address', 'email', 'property_type')