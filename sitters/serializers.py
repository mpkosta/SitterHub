from rest_framework import serializers
from .models import Sitter

class SitterSerializer(serializers.ModelSerializer):
    user_email = serializers.EmailField(source='user.email', read_only=True)

    class Meta:
        model = Sitter
        fields = [
            'id',
            'sitter_first_name',
            'sitter_last_name',
            'user_email',
            'bio',
            'experience',
            'hourly_rate'
        ]
        read_only_fields = ['id']