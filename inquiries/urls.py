from django.urls import path
from . import views

urlpatterns = [
    path('create/<int:sitter_id>/', views.create_inquiry, name='inquiry-create'),
    path('', views.InquiryListView.as_view(), name='inquiry-list'),
    path('<int:pk>/edit/', views.InquiryUpdateView.as_view(), name='inquiry-edit'),
    path('<int:pk>/delete/', views.InquiryDeleteView.as_view(), name='inquiry-delete'),
]