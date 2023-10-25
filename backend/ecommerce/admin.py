from . import models
from django.contrib import admin


@admin.register(models.Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("id", "title")


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "item")
