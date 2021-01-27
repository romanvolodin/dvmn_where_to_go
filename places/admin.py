from django.contrib import admin
from .models import (
    Place,
    Image,
)


class ImageInlineAdmin(admin.TabularInline):
    model = Image


class PlaceAdmin(admin.ModelAdmin):
    model = Place
    inlines = [ImageInlineAdmin] 

admin.site.register(Place, PlaceAdmin)
admin.site.register(Image)