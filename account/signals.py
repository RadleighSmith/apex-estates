from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
from django.contrib import messages


@receiver(user_logged_in)
def user_logged_in_handler(sender, request, user, **kwargs):
    """
    Signal receiver for user login events.

    This function handles the 'user_logged_in' signal, which is triggered
    when a user successfully logs in. Upon receiving this signal, it displays
    a success message to the user indicating a successful login.
    """
    messages.success(request, 'You have successfully logged in!')


@receiver(user_logged_out)
def user_logged_out_handler(sender, request, user, **kwargs):
    """
    Signal receiver for user logout events.

    This function handles the 'user_logged_out' signal, which is triggered
    when a user logs out. Upon receiving this signal, it displays a success
    message to the user indicating a successful logout.
    """
    messages.success(request, 'You have been successfully logged out!')
