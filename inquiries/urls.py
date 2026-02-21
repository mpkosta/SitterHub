from django.urls import path
from . import views

urlpatterns = [
    path('create/<int:sitter_id>/', views.create_inquiry, name='inquiry-create'),
]