from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.humanize.templatetags.humanize import intcomma
from django.core.paginator import Paginator
from property.models import Property
from .forms import RegisterForm

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

    return render(request, 'dashboard/dashboard.html', {'page_obj': page_obj})