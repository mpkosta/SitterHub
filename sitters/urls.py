from django.urls import path
from .views import SitterListView, SitterDetailView

urlpatterns = [
    path('', SitterListView.as_view(), name='sitters-list'),
    path('<int:pk>/', SitterDetailView.as_view(), name='sitter-profile'),
]