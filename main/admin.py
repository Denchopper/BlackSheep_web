from django.contrib import admin
from .models import *


@admin.register(SportType)
class SportTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'type', 'date']
    list_filter = ['type']
