from django.urls import path, include
from .views import get_event

urlpatterns = [
    path('', get_event),
    path('shop/', include('shop.urls')),
]
