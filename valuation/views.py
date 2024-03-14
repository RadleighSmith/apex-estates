from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ValuationRequestForm


def valuation_request(request):
    """
    View for handling valuation requests.

    This view function handles both GET and POST requests for submitting
    valuation requests. If the request method is POST and the form data is
    valid, the valuation request is saved and a success message is displayed.
    If the form data is invalid, the form is re-rendered with error messages.
    For GET requests, the view renders the valuation request form.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object rendering the valuation request
        form or redirecting to the valuation request page.
    """
    if request.method == 'POST':
        form = ValuationRequestForm(request.POST)
        if form.is_valid():
            form.save()
            success_message = 'Thank you! We have received your valuation ' \
                              'request. We will contact you shortly.'
            messages.success(request, success_message)
            return redirect('valuation_request')
    else:
        form = ValuationRequestForm()
    return render(request, 'valuation.html', {'form': form})
