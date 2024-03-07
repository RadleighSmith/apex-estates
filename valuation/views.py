from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ValuationRequestForm

def valuation_request(request):
    if request.method == 'POST':
        form = ValuationRequestForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you! We have received your valuation request. We will contact you shortly.')
            return redirect('valuation_request')
    else:
        form = ValuationRequestForm()
    return render(request, 'valuation.html', {'form': form})
