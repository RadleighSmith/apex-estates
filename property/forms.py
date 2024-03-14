from django import forms
from .models import Property


class PropertyForm(forms.ModelForm):
    """
    Form for creating or updating a property.

    This form extends the ModelForm class and is used to create or update
    Property objects. It includes fields for the title, main image, property
    type, address, price, number of bedrooms, number of bathrooms, garage
    availability, parking availability, and description of the property.

    Attributes:
        description (forms.CharField): A CharField widget with a TextArea
            attribute to allow multi-line input for the property description.
    """

    description = forms.CharField(widget=forms.Textarea(attrs={'id': 'description'}))

    class Meta:
        """
        Meta class specifying the model and fields for the form.

        Attributes:
            model (class): The model class to be used for the form.
            fields (list): A list of field names to include in the form.
            widgets (dict): A dictionary specifying custom widgets for form
                fields.
        """

        model = Property
        fields = ['title', 'main_image', 'property_type', 'address', 'price',
                  'bedrooms', 'bathrooms', 'garage', 'parking', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'maxlength': 200}),
            'address': forms.TextInput(attrs={'maxlength': 100}),
        }
