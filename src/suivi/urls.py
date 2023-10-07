from django.urls import path
from .views import index, update_series

urlpatterns = [
    path('', index, name="suivi-index"),
    path('update_series/<int:serie_id>', update_series, name='update_series')
]