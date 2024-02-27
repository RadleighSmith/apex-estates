from django.contrib import admin
from .models import Property
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Property)
class PropertyAdmin(SummernoteModelAdmin):
    list_display = ('title', 'address', 'price', 'property_type', 'listed_on', 'updated_on', 'total_favorites')
    search_fields = ['title', 'address']
    list_filter = ('property_type', 'parking', 'garage')
    summernote_fields = ('description',)
    
    def total_favorites(self, obj):
        return obj.favourite_set.count()
    total_favorites.short_description = "Total Favorites"