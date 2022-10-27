from django.shortcuts import render
from django.http import HttpResponse
from .models import Beer


def home(request):
    return HttpResponse('<h3>Магазин<h3>')


def shop(request):
    beers = Beer.objects.order_by('-available')
    return render(request, 'shop/index.html', {'beers': beers, "title": "Ассортимент"})
