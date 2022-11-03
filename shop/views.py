from django.shortcuts import render
from django.http import HttpResponse
from .models import Beer, BeerStyle


def home(request):
    return render(request, 'base.html')


def shop(request):
    beer = Beer.objects.order_by('-available')
    beer_style = BeerStyle.objects.all
    return render(request, 'shop/index.html', {'beer': beer, "title": "Ассортимент", 'beer_style': beer_style})


def get_style(request, beer_style_id):
    beer = Beer.objects.filter(beer_style_id=beer_style_id)
    beer_style = BeerStyle.objects.all()
    style = BeerStyle.objects.get(pk=beer_style_id)
    return render(request, 'shop/style.html', {'beer': beer, 'beer_style': beer_style, 'style': style})
