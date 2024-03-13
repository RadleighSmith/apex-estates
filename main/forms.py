from django import forms
from .models import Message, NewsletterSignUp


class MessageForm(forms.ModelForm):
    """
    Form for submitting a message through the contact form.

    This form allows users to submit their first name, last name,
    email address, and message content.

    Attributes:
        first_name (str): The first name of the sender.
        last_name (str): The last name of the sender.
        email (str): The email address of the sender.
        message (str): The content of the message.
    """
    class Meta:
        model = Message
        fields = ['first_name', 'last_name', 'email', 'message']


class NewsletterSubscriptionForm(forms.ModelForm):
    """
    Form for newsletter subscription.

    This form allows users to subscribe to the newsletter by providing their
    email address.

    Attributes:
        email (str): The email address of the user subscribing to the
        newsletter.
    """
    class Meta:
        model = NewsletterSignUp
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={'autocomplete': 'on'})
        }
