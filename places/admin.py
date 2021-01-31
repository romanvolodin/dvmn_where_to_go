from django.contrib import admin
from django.utils.safestring import mark_safe
from adminsortable2.admin import SortableInlineAdminMixin
from .models import (
    Place,
    Image,
)


class ImageInlineAdmin(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    fields = ("image", "get_preview", "order",)
    readonly_fields = ("get_preview",)

    def get_preview(self, obj):
        return mark_safe(f"<img src='{obj.image.url}' height='200'>")

    get_preview.short_description = "Превью" 


class PlaceAdmin(admin.ModelAdmin):
    model = Place
    inlines = [ImageInlineAdmin] 

admin.site.register(Place, PlaceAdmin)
admin.site.register(Image)