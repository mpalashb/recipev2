"""
API view for user
"""
from rest_framework.generics import (
    CreateAPIView,
)
from user.serializers import UserSerialzer


class CreateUserView(CreateAPIView):
    """Create new user"""

    serializer_class = UserSerialzer
