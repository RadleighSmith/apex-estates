from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.humanize.templatetags.humanize import intcomma
from django.core.paginator import Paginator
from property.models import Property

# Create your views here.

def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = RegisterForm()

    return render(request, 'registration/sign_up.html', {'form': form})

@login_required
def user_dashboard(request):
    user_favourites = Property.objects.filter(favourite=request.user)
    paginator = Paginator(user_favourites, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Add formatted_price and is_favourite attributes to each property in user_favourites queryset
    for property in page_obj.object_list:
        property.formatted_price = intcomma(property.price)
        property.is_favourite = True  # Assuming all properties in user_favourites are already favorited by the user

    return render(request, 'dashboard/dashboard.html', {'page_obj': page_obj})