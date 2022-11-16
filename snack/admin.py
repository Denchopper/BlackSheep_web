from django.contrib import admin
from .models import Snack, SnackType


@admin.register(SnackType)
class SnackTypeAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Snack)
class SnackAdmin(admin.ModelAdmin):
    list_display = ['name', 'type', 'price_per_100g', 'available']
    list_editable = ['price_per_100g', 'available']

