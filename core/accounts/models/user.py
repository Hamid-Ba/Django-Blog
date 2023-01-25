from django.db import models
from django.contrib.auth.models import (AbstractBaseUser,PermissionsMixin,BaseUserManager)

class UserManager(BaseUserManager):
    """User Manager"""
    def create_user(self,email,password,**extra):
        """Create User Method"""
        if not email :
            raise ValueError("Email Must Be Set")
        email = self.normalize_email(email)
        
        user = self.model(email=email,**extra)
        user.set_password(password)
        user.save()
        
        return user

    def create_superuser(self,email,password,**extra):
        """Create Superuser Method"""
        extra.setdefault('is_staff',True)
        extra.setdefault('is_superuser',True)
        extra.setdefault('is_active',True)

        if extra.get('is_staff') is not True :
            raise ValueError("Super User Must Have is_staff = True")
        if extra.get('is_superuser') is not True :
            raise ValueError("Super User Must Have is_superuser = True")

        return self.create_user(email,password,**extra)

class User(AbstractBaseUser,PermissionsMixin):
    """User Model"""
    email = models.EmailField(max_length=255,unique=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    created_data = models.DateTimeField(auto_now_add=True)
    updated_data = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'

    def __str__(self) -> str:
        return self.email

    objects = UserManager()