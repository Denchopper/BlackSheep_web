from django.urls import path, include
from .views import get_event, contact_us

urlpatterns = [
    path('', get_event, name='main'),
    path('shop/', include('shop.urls')),
    path('snack/', include('snack.urls')),
    path('contact_us/', contact_us)
]
