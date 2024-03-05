from django.shortcuts import render
from django.contrib.humanize.templatetags.humanize import intcomma
from property.models import Property

# Create your views here.

def home(request):
    latest_properties = Property.objects.order_by('-listed_on')[:4]
    for property in latest_properties:
        property.formatted_price = intcomma(property.price)
        if request.user.is_authenticated:
            property.is_favourite = property.favourite.filter(id=request.user.id).exists()
        else:
            property.is_favourite = False
    return render(request, 'index.html', {'latest_properties': latest_properties})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')