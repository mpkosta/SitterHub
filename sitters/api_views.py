from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Sitter
from .serializers import SitterSerializer

class SitterListApiView(ListAPIView):
    queryset = Sitter.objects.all()
    serializer_class = SitterSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class SitterDetailApiView(RetrieveAPIView):
    queryset = Sitter.objects.all()
    serializer_class = SitterSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]