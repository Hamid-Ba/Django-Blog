from django.urls import path, include

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from accounts.api.v1 import views

urlpatterns = [
    # Auth URLs
    path("register/", views.RegisterView.as_view(), name="register"),
    path(
        "verification/<str:token>/",
        views.VerifyView.as_view(),
        name="verification",
    ),
    path(
        "change_password/",
        views.ChangePasswordView.as_view(),
        name="change_password",
    ),
    # JWT Authentication URLs
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify_token/", TokenVerifyView.as_view(), name="token_verify"),
    # Use URLs
    path("profile/", views.ProfileView.as_view(), name="profile"),
]
