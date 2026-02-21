from django.urls import path
from . import views

urlpatterns = [
    path('apply/', views.ApplicationCreateView.as_view(), name='apply'),
    path('applications/', views.ApplicationListView.as_view(), name='application-list'),
    path('applications/<int:pk>/edit/', views.ApplicationUpdateView.as_view(), name='application-edit'),
    path('applications/<int:pk>/delete/', views.ApplicationDeleteView.as_view(), name='application-delete'),
]