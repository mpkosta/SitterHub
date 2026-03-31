from django.contrib import admin
from .models import Sitter, Language


@admin.register(Sitter)
class SitterAdmin(admin.ModelAdmin):
    list_display = (
        "sitter_first_name",
        "sitter_last_name",
        "hourly_rate",
        "experience",)
    search_fields = (
        "sitter_first_name",
        "sitter_last_name")
    filter_horizontal = (
        "services",
        "languages")

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ("language_name",)
    search_fields = ("language_name",)