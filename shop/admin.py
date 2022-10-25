from django.contrib import admin
from .models import BeerType, Brewery, BeerStyle, SnackType, Beer, BeerVolume, Snack


# admin.site.register(BeerType)
@admin.register(BeerType)
class BeerTypeAdmin(admin.ModelAdmin):
    pass


# admin.site.register(Brewery)
@admin.register(Brewery)
class BreweryAdmin(admin.ModelAdmin):
    pass


# admin.site.register(BeerStyle)
@admin.register(BeerStyle)
class BeerStyleAdmin(admin.ModelAdmin):
    pass


# admin.site.register(SnackType)
@admin.register(SnackType)
class SnackTypeAdmin(admin.ModelAdmin):
    pass


# admin.site.register(Beer)
@admin.register(Beer)
class BeerAdmin(admin.ModelAdmin):
    list_display = ['name', 'brewery', 'beer_style', 'beer_type', 'price_per_05', 'available']
    list_editable = ['price_per_05', 'available']


# admin.site.register(BeerVolume)
@admin.register(BeerVolume)
class BeerVolumeAdmin(admin.ModelAdmin):
    pass


# admin.site.register(Options)
"""@admin.register(Options)
class OptionsAdmin(admin.ModelAdmin):
    pass"""


# admin.site.register(Snack)
@admin.register(Snack)
class SnackAdmin(admin.ModelAdmin):
    list_display = ['name', 'type', 'price_per_100g', 'available']
    list_editable = ['price_per_100g', 'available']
