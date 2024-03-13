from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    """
    Custom registration form that extends Django's UserCreationForm
    and adds additional fields for first name, last name, and email.

    Upon saving, it sets the username as the email address provided.
    """
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "password1", "password2"]

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.username = self.cleaned_data['email']
        if commit:
            user.save()
        return user
