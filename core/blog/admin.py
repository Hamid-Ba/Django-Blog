from django.contrib import admin
from .models import Post, Category


class PostAdmin(admin.ModelAdmin):
    """Post Admin Model"""

    list_display = ["title", "status", "published_data", "author", "category"]
    list_display_links = ["title", "author", "category"]

    search_fields = ["title", "author__email", "category__name"]


admin.site.register(Category)
admin.site.register(Post, PostAdmin)
