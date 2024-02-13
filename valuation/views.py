from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def valuation_request(request):
    return HttpResponse("This will be the valuation requests page")