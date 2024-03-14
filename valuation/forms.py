from django import forms
from .models import ValuationRequest


class ValuationRequestForm(forms.ModelForm):
    """
    Form for creating a valuation request.

    This form extends the ModelForm class and is used to create
    ValuationRequest objects. It includes fields for the name of the
    requester, contact number, property address, email, and property type.

    Attributes:
        model (class): The model class to be used for the form.
        fields (list): A list of field names to include in the form.
    """

    class Meta:
        """
        Meta class specifying the model and fields for the form.

        Attributes:
            model (class): The model class to be used for the form.
            fields (list): A list of field names to include in the form.
        """

        model = ValuationRequest
        fields = [
            'name',
            'contact_number',
            'property_address',
            'email',
            'property_type'
        ]
