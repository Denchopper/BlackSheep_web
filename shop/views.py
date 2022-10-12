from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('<h3>Головна сторінка<h3>')


def shop(request):
    return HttpResponse('<h3>Магазин<h3>')
