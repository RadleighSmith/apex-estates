from django import forms
from .models import Property

class PropertyForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={'id': 'description'}))
    
    class Meta:
        model = Property
        fields = ['title', 'main_image', 'property_type', 'address', 'price', 'bedrooms', 'bathrooms', 'garage', 'parking', 'description']