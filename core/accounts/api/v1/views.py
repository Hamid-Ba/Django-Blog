from rest_framework import generics , views , permissions , authentication , status
from rest_framework.response import Response
from rest_framework_simplejwt import authentication as jwtAuth

from . import serializers
from ... import models

class RegisterView(generics.CreateAPIView):
    """Register View"""
    permission_classes = [permissions.AllowAny]
    serializer_class = serializers.RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,context={'request':self.request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response('Please confirm your email address to complete the registration',status=status.HTTP_201_CREATED)

class ChangePasswordView(generics.GenericAPIView):
    """Change Password View"""
    serializer_class = serializers.ChangePasswordSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [jwtAuth.JWTAuthentication]

    def put(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,instance=self.request.user,context={'request':self.request})
        serializer.is_valid(raise_exception=True)
        return Response({"detail" : "your password changed successfully"},status=status.HTTP_200_OK)

class ProfileView(generics.RetrieveUpdateAPIView):
    """Profile View"""
    serializer_class = serializers.ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [jwtAuth.JWTAuthentication]

    def get_object(self):
        return models.Profile.objects.get(user=self.request.user)


# when user registered , the acc would be created but not verified 
# then send an email to user email for verification
# the verification email is a jwt code that we would've generated for the user and it contains the user id
# so by clicking the link who we've generated , user would be redirected to an url which make user acc verified