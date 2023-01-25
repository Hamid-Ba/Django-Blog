from rest_framework import generics , views , permissions , authentication
from rest_framework.response import Response
from rest_framework_simplejwt import authentication as jwtAuth

from . import serializers

class RegisterView(generics.CreateAPIView):
    """Register View"""
    serializer_class = serializers.RegisterSerializer