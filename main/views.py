from django.shortcuts import render
from .models import *


def get_event(request):
    event = Event.objects.all()
    return render(request, 'main/main.html', {'event': event, 'title': 'SPORT EVENTS'})
