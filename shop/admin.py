from django.contrib import admin
from .models import BeerType, Brewery, BeerStyle, SnackType, Beer, BeerVolume, Options, Snack

admin.site.register(BeerType)
admin.site.register(Brewery)
admin.site.register(BeerStyle)
admin.site.register(SnackType)
admin.site.register(Beer)
admin.site.register(BeerVolume)
admin.site.register(Options)
admin.site.register(Snack)
