from django.urls import path
from .views import SitterListView, SitterDetailView, SitterUpdateView, SitterCreateView

urlpatterns = [
    path('', SitterListView.as_view(), name='sitters-list'),
    path('add/', SitterCreateView.as_view(), name='sitter-create'),
    path('<int:pk>/', SitterDetailView.as_view(), name='sitter-profile'),
    path('<int:pk>/edit/', SitterUpdateView.as_view(), name='sitter-edit'),
]