from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
from django.contrib import messages

@receiver(user_logged_in)
def user_logged_in_handler(sender, request, user, **kwargs):
    messages.success(request, 'You have successfully logged in!')

@receiver(user_logged_out)
def user_logged_out_handler(sender, request, user, **kwargs):
    messages.success(request, 'You have been successfully logged out!')
