from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from django.contrib.humanize.templatetags.humanize import intcomma
from django.core.paginator import Paginator
from property.models import Property
from .forms import RegisterForm
from main.models import Message
from valuation.models import ValuationRequest

# Create your views here.

def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'You have successfully signed up!')
            return redirect('/')
        else:
            messages.error(request, 'There was an error with your sign-up. Please try again.')
    else:
        form = RegisterForm()

    return render(request, 'registration/sign_up.html', {'form': form})

@login_required
def user_dashboard(request):
    user_favourites = Property.objects.filter(favourite=request.user)
    paginator = Paginator(user_favourites, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    for property in page_obj.object_list:
        property.formatted_price = intcomma(property.price)
        property.is_favourite = True

    user_messages = []
    requested_valuations = []

    # Fetch messages if user is superuser or staff
    if request.user.is_superuser or request.user.is_staff:
        user_messages = Message.objects.all()

    # Fetch valuation requests for all users
    requested_valuations = ValuationRequest.objects.all()

    return render(request, 'dashboard/dashboard.html', {
        'page_obj': page_obj,
        'user_messages': user_messages,
        'requested_valuations': requested_valuations,
    })

@login_required
@staff_member_required
def delete_message(request, message_id):
    message = get_object_or_404(Message, pk=message_id)
    if request.method == 'POST':
        message.delete()
        return redirect('dashboard')

@login_required
@staff_member_required
def delete_valuation(request, valuation_id):
    valuation = get_object_or_404(ValuationRequest, pk=valuation_id)
    if request.method == 'POST':
        valuation.delete()
        return redirect('dashboard')