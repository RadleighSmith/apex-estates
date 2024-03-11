from django.shortcuts import render


def apex_404_page(request, exception):
    """ 404 ERROR page """
    return render(request, '404.html', status=404)


def apex_500_page(request):
    """ 500 ERROR page """
    return render(request, '500.html', status=500)