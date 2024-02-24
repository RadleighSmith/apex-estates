from django.shortcuts import render
from property.models import Property

# Create your views here.

def home(request):
    latest_properties = Property.objects.order_by('-listed_on')[:3]
    return render(request, 'index.html', {'latest_properties': latest_properties})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')