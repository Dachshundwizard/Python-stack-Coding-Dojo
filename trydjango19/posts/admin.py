from django.contrib import admin

# Register your models here.
from .models import Post # This is a relative import

class PostModelAdmin(admin.ModelAdmin): # ModelAdmin is refering to the Post model.
    list_display = ["__unicode__", "timestamp", "updated"]
    list_filter = ["updated", "timestamp", "title"]
    search_fields = ["title", "content"]
    class Meta:
        model = Post # Refering to the Post Model specifically

admin.site.register(Post, PostModelAdmin) # Connects Post Model to PostModelAdmin
