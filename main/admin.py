from django.contrib import admin
from .models import Message

class MessageAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'created_at')
    search_fields = ('first_name', 'last_name', 'email', 'message')

admin.site.register(Message, MessageAdmin)
