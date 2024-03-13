from django import forms
from .models import Message, NewsletterSignUp

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['first_name', 'last_name', 'email', 'message']

class NewsletterSubscriptionForm(forms.ModelForm):
    class Meta:
        model = NewsletterSignUp
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={'autocomplete': 'on'})
        }