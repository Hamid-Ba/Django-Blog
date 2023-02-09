from django.db import models
from django.contrib.auth import get_user_model


class Profile(models.Model):
    """Profile Model"""

    first_name = models.CharField(max_length=225)
    last_name = models.CharField(max_length=225)
    avatar = models.ImageField(null=True, blank=True)
    bio = models.CharField(max_length=500)

    created_data = models.DateTimeField(auto_now_add=True)
    updated_data = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.email
