from django.contrib import admin
from .models import Application

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'application_status',
        'created_at',
    )

    list_filter = (
        'application_status',
        'created_at'
    )
    search_fields = (
        'first_name',
        'last_name',
        'email',
        'phone_number',
    )
    list_editable = ('application_status',)