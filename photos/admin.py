from django.contrib import admin
from .models import Photo, Category, Comment
# Register your models here.
admin.site.register(Photo)
admin.site.register(Category)
admin.site.register(Comment)
