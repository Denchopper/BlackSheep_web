from django.shortcuts import render
from .models import *


def snack_shop(request):
    snack = Snack.objects.all()
    snack_type = SnackType.objects.all
    return render(request, 'snack/snack_index.html', {'snack': snack, "title": "Snacks", 'snack_type': snack_type})


def get_snack_type(request, snack_type_id):
    snack = Snack.objects.filter(snack_type_id=snack_type_id)
    snack_type = SnackType.objects.all()
    type = SnackType.objects.get(pk=snack_type_id)
    return render(request, 'snack/type.html', {'snack': snack, 'snack_type': snack_type, 'type': type})
