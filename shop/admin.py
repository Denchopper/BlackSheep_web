from django.contrib import admin
from .models import BeerType, Brewery, BeerStyle, SnackType, Beer

admin.site.register(BeerType)
admin.site.register(Brewery)
admin.site.register(BeerStyle)
admin.site.register(SnackType)
admin.site.register(Beer)