from adminsortable2.admin import SortableInlineAdminMixin
from django.contrib import admin
from django.utils.html import format_html

from .models import Image, Place


class ImageInlineAdmin(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    fields = ("image", "get_preview", "order",)
    readonly_fields = ("get_preview",)

    def get_preview(self, obj):
        if not obj.image:
            return format_html("Здесь будет превью, когда вы загрузите файл.")
        return format_html("<img src='{}' height='200'>", obj.image.url)

    get_preview.short_description = "Превью" 


class PlaceAdmin(admin.ModelAdmin):
    model = Place
    inlines = [ImageInlineAdmin] 

admin.site.register(Place, PlaceAdmin)
admin.site.register(Image)