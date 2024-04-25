from django.contrib import admin
from .models import *
from django.utils.html import mark_safe
from . import models


class PhotoInline(admin.TabularInline):

    model = models.Photo


class SpecificationInline(admin.TabularInline):

    model = models.Specification



@admin.register(models.Products)
class RoomAdmin(admin.ModelAdmin):

    """ Room Admin Definition """

    inlines = (PhotoInline, SpecificationInline)

    fieldsets = (
        (
            "Basic Info",
            {"fields": ("name", "price", "description",)},
        ),
    )

    ordering = ("name", "price")

    list_display = (
        "name",
        "price",
        "description",
        "video_link",
        "count_photos",
    )

    list_filter = (
        "price",
        "name",
    )

    search_fields = ("=name", "^price")

    def count_photos(self, obj):
        return obj.photos.count()

    count_photos.short_description = "Photo Count"




@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """ Photo Admin Definition """

    list_display = ("__str__", "get_thumbnail")

    def get_thumbnail(self, obj):
        return mark_safe(f'<img width="50px" src="{obj.file.url}" />')

    get_thumbnail.short_description = "Thumbnail"