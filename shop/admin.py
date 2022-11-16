from django.contrib import admin
from .models import BeerType, Brewery, BeerStyle, Beer, BeerVolume


@admin.register(BeerType)
class BeerTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Brewery)
class BreweryAdmin(admin.ModelAdmin):
    pass


@admin.register(BeerStyle)
class BeerStyleAdmin(admin.ModelAdmin):
    pass


@admin.register(Beer)
class BeerAdmin(admin.ModelAdmin):
    list_display = ['name', 'brewery', 'beer_style', 'beer_type', 'price_per_05', 'available']
    list_editable = ['price_per_05', 'available']
    search_fields = ['name']
    list_filter = ['available', 'brewery', 'beer_style']


@admin.register(BeerVolume)
class BeerVolumeAdmin(admin.ModelAdmin):
    pass
