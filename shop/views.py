from django.shortcuts import render
from django.views.generic import ListView
from .models import Beer, BeerStyle


def home(request):
    return render(request, 'base.html')


class Shop(ListView):
    model = Beer
    template_name = 'shop/index.html'
    context_object_name = 'beer'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['beer_style'] = BeerStyle.objects.all
        return context

    def get_queryset(self):
        return Beer.objects.filter(available=True)


def get_style(request, beer_style_id):
    beer = Beer.objects.filter(beer_style_id=beer_style_id)
    beer_style = BeerStyle.objects.all()
    style = BeerStyle.objects.get(pk=beer_style_id)
    return render(request, 'shop/style.html', {'beer': beer, 'beer_style': beer_style, 'style': style})

# class BeerByStyle(ListView):
#     model = BeerStyle
#     template_name = 'shop/style.html'
#     context_object_name = 'beer_style'
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['beer_style'] = BeerStyle.objects.all
#         return context
#
#     def get_queryset(self):
#         return BeerStyle.objects.filter(beer_style_id=self.kwargs['beer_style_id'])
