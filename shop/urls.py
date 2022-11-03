from django.urls import path
from . import views
from .views import get_style

urlpatterns = [
    path('', views.shop),
    path('<int:beer_style_id>/', get_style),
]
