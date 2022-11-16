from django.urls import path
from . import views
from .views import get_snack_type

urlpatterns = [
    path('', views.snack_shop),
    path('<int:snack_type_id>/', get_snack_type, name='snack_type')]
