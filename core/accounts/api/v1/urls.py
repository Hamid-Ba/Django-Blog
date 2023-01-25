from django.urls import path , include
from rest_framework.routers import DefaultRouter

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

from . import views

urlpatterns = [
    # Auth URLs
    path('register/',views.RegisterView.as_view(),name='register'),
    path('change_password/',views.ChangePasswordView.as_view(),name='change_password'),
    # JWT Authentication URLs
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify_token/', TokenVerifyView.as_view(), name='token_verify'),

    # Use URLs
    path('profile/',views.ProfileView.as_view(), name='profile'),
]