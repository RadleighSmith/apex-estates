"""
URL configuration for apex_estates project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404, handler500
from .views import apex_404_page, apex_500_page


urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('', include('main.urls')),
    path('', include('property.urls')),
    path('', include('account.urls')),
    path('', include('valuation.urls')),
    path('', include('django.contrib.auth.urls')),
]

# Admin Site title
admin.site.site_header = "Apex Estates"
admin.site.site_title = "Apex Estates Administration"

# Error Pages
handler404 = apex_404_page
handler500 = apex_500_page
