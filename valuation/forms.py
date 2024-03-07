from django import forms
from .models import ValuationRequest

class ValuationRequestForm(forms.ModelForm):
    class Meta:
        model = ValuationRequest
        fields = ['name', 'contact_number', 'property_address', 'email', 'property_type']