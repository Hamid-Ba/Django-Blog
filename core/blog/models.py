from django.db import models
import core.settings as sting

class Post(models.Model):
    """Blog Model"""
    image = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=125)
    content = models.TextField()
    status = models.BooleanField()
    published_data = models.DateTimeField()

    auhtor = models.ForeignKey(sting.AUTH_USER_MODEL,on_delete=models.CASCADE)
    category = models.ForeignKey('Category',on_delete=models.SET_NULL,null=True)

    created_data = models.DateTimeField(auto_now_add=True)
    updated_data = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title

class Category(models.Model):
    """Category Model"""
    name = models.CharField(max_length=85)

    def __str__(self) -> str:
        return self.name