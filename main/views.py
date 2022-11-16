from django.shortcuts import render, redirect
from .models import *
from .forms import ContactUsForm


def get_event(request):
    event = Event.objects.all()
    return render(request, 'main/main.html', {'event': event, 'title': 'SPORT EVENTS'})


def contact_us(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form =form.save()
            #ContactUs.objects.create(**form.cleaned_data)
            return redirect('/')
    else:
        form = ContactUsForm()
    return render(request, 'main/contact-us.html', {'form': form})
