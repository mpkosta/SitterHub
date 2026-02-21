from django.urls import path
from .views import SitterListView

urlpatterns = [
    path('', SitterListView.as_view(), name='sitters-list'),
]