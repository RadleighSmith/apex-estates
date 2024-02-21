from django.contrib import admin
from .models import Property
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Property)
class PropertyAdmin(SummernoteModelAdmin):
    list_display = ('title', 'address', 'price', 'property_type', 'parking', 'garage')
    search_fields = ['title', 'address']
    list_filter = ('property_type', 'parking', 'garage')
    summernote_fields = ('description',)