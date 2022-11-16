from django.urls import path
# from . import views
from .views import Shop, get_style

urlpatterns = [
    path('', Shop.as_view(), name='beer', ),
    path('<int:beer_style_id>/',  get_style, name='style'),
    # path('<int:beer_style_id>/', BeerByStyle.as_view(), name='style')
]
