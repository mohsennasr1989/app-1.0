from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """Serializer for users object"""

    class Meta:
        model = get_user_model()
        fields = {'name', 'email', 'password'}
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}

    def create(self, validate_data):
        """Create new user with encrypted password and return it"""
        return get_user_model().objects.create_user(**validate_data)