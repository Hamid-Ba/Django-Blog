from rest_framework.generics import CreateAPIView

from . import serializers

class RegisterView(CreateAPIView):
    """Register View"""
    serializer_class = serializers.RegisterSerializer