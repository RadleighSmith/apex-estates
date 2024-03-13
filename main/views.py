from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.humanize.templatetags.humanize import intcomma
from property.models import Property
from .forms import MessageForm, NewsletterSubscriptionForm


def home(request):
    """
    View function for the home page.

    Renders the home page with the latest properties and a newsletter
    subscription form. If the form is submitted successfully, the user
    is signed up for the newsletter.
    """
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
    """
    View function for the about page.

    Renders the about page.
    """
    return render(request, 'about.html')


def contact(request):
    """
    View function for the contact page.

    Renders the contact page with a message form.
    """
    form = MessageForm()
    return render(request, 'contact.html', {
        'form': form
    })


def send_message(request):
    """
    View function to handle sending a message.

    If the request method is POST and the form is valid, the message is saved.
    Otherwise, an error message is displayed.
    """
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
