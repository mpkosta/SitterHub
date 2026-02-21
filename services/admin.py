from django.contrib import admin
from .models import ServiceGroup


@admin.register(ServiceGroup)
class ServiceGroupAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "slug")
    prepopulated_fields = {"slug": ("name",)}