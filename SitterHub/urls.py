from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from sitters.api_views import SitterListApiView, SitterDetailApiView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('common.urls')),
    path('sitters/', include('sitters.urls')),
    path('inquiry/', include('inquiries.urls')),
    path('applications/', include('recruitment.urls')),
    path('accounts/', include('accounts.urls')),
    path('api/sitters/', SitterListApiView.as_view(), name='api-sitters-list'),
    path('api/sitters/<int:pk>/', SitterDetailApiView.as_view(), name='api-sitter-detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)