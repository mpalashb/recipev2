"""
Serializers for the user API
"""
from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserSerialzer(serializers.ModelSerializer):
    """Serializer class for the user model"""

    class Meta:
        model = get_user_model()
        fields = ["pk", "email", "password"]
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}

    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)
