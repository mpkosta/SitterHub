from django.contrib import admin
from .models import Inquiry

@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = ('client_first_name', 'client_last_name', 'sitter', 'created_at')
    list_filter = ('created_at', 'sitter')
    search_fields = ('client_first_name', 'client_last_name', 'client_email')