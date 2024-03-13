from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from django.contrib.humanize.templatetags.humanize import intcomma
from django.core.paginator import Paginator

from property.models import Property
from main.models import Message
from valuation.models import ValuationRequest
from .forms import RegisterForm


def sign_up(request):
    """
    View function for user sign-up.

    This function handles user sign-up requests. If the request method is POST
    and the form data is valid, a new user is registered and logged in. Upon
    successful sign-up, a success message is displayed. If the form data is
    invalid, an error message is displayed to prompt the user to try again.
    """
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            try:
                user = form.save()
                login(request, user)
                messages.success(request, 'You have successfully signed up!')
                return redirect('/')
            except IntegrityError:
                form.add_error('email', 'This email is already in use.')
        else:
            messages.error(request,
                           'There was an error with your sign-up. '
                           'Please try again.')
    else:
        form = RegisterForm()

    return render(request, 'registration/sign_up.html', {'form': form})


@login_required
def user_dashboard(request):
    """
    View function for user dashboard.

    This function displays the user's dashboard, including their favourite
    properties, messages, and requested valuations. Superusers and staff
    members have access to all messages and valuation requests.
    """
    user_favourites = Property.objects.filter(favourite=request.user)
    paginator = Paginator(user_favourites, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    for property in page_obj.object_list:
        property.formatted_price = intcomma(property.price)
        property.is_favourite = True

    user_messages = []
    requested_valuations = []

    if request.user.is_superuser or request.user.is_staff:
        user_messages = Message.objects.all()

    requested_valuations = ValuationRequest.objects.all()

    return render(request, 'dashboard/dashboard.html', {
        'page_obj': page_obj,
        'user_messages': user_messages,
        'requested_valuations': requested_valuations,
    })


@login_required
@staff_member_required
def delete_message(request, message_id):
    """
    View function to delete a message.

    This function allows staff members to delete a specific message.
    Upon successful deletion, a success message is displayed to the user.
    """
    message = get_object_or_404(Message, pk=message_id)
    if request.method == 'POST':
        message.delete()
        messages.success(request, 'Message Deleted')
        return redirect('dashboard')


@login_required
@staff_member_required
def delete_valuation(request, valuation_id):
    """
    View function to delete a valuation request.

    This function allows staff members to delete a specific valuation
    request. Upon successful deletion, a success message is displayed to the
    user.
    """
    valuation = get_object_or_404(ValuationRequest, pk=valuation_id)
    if request.method == 'POST':
        valuation.delete()
        messages.success(request, 'Valuation Deleted')
        return redirect('dashboard')
