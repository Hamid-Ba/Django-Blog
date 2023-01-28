from rest_framework import generics , views , permissions , authentication , status
from rest_framework.response import Response
from rest_framework_simplejwt import authentication as jwtAuth
import jwt
from jwt.exceptions import ExpiredSignatureError, InvalidSignatureError
from django.contrib.auth import get_user_model
from django.conf import settings
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie, vary_on_headers

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

class VerifyView(views.APIView):
    """Verify View"""
    permission_classes = [permissions.AllowAny]

    def get(self, request,token):
        simple_jwt = settings.SIMPLE_JWT
        try :
            res = jwt.decode(token,simple_jwt['SIGNING_KEY'],simple_jwt['ALGORITHM'])
            user = get_user_model().objects.get(id=res['user_id'])
            if user.is_verified: return Response({"details": "your account has already been verified"})
     
            user.is_verified = True
            user.save()
            return Response({'detail' : 'your account verified successfully'},status=status.HTTP_200_OK)
        except ExpiredSignatureError as e:
            return Response({'detail' : 'Your Verification Code Has Been Expired!'},status=status.HTTP_400_BAD_REQUEST)
        except InvalidSignatureError as e:
            return Response({'detail' : 'Your Verification Code is Not Valid!'},status=status.HTTP_400_BAD_REQUEST)

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

    # if user is authenticated cached his/her profile for 2 hours
    @method_decorator(cache_page(60*60*2))
    @method_decorator(vary_on_headers("Authorization",))
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)