from django.shortcuts import render


# Create your views here.
def property_listings(request):
    return render(request, 'property_listings.html')