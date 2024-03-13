from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.humanize.templatetags.humanize import intcomma
from property.models import Property
from .forms import MessageForm, NewsletterSubscriptionForm


def home(request):
    latest_properties = Property.objects.order_by('-listed_on')[:4]
    for property in latest_properties:
        property.formatted_price = intcomma(property.price)
        if request.user.is_authenticated:
            property.is_favourite = property.favourite.filter(
                id=request.user.id).exists()
        else:
            property.is_favourite = False

    if request.method == 'POST':
        form = NewsletterSubscriptionForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'You have successfully signed up '
                                 'for the newsletter!')
                return redirect('home')
            except ValueError:
                messages.error(request, 'You have already signed up for '
                               'the newsletter!')
                return redirect('home')
    else:
        form = NewsletterSubscriptionForm()

    return render(request, 'index.html', {
        'latest_properties': latest_properties,
        'form': form
    })


def about(request):
    return render(request, 'about.html')


def contact(request):
    form = MessageForm()
    return render(request, 'contact.html', {
        'form': form
    })


def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent '
                             'successfully!')
            return redirect('contact_us')
    else:
        messages.error(request, 'There was an error with your message. '
                                'Please try again.')
    return HttpResponse("Invalid request method", status=400)
