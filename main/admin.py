from django.contrib import admin
from .models import Message, NewsletterSignUp


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'created_at')
    search_fields = ('first_name', 'last_name', 'email', 'message')


@admin.register(NewsletterSignUp)
class NewsletterSignUpAdmin(admin.ModelAdmin):
    list_display = ('email', 'sign_up_date')
