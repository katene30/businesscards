# cards/urls.py
from django.urls import path
from .views import card_list

urlpatterns = [
    path('', card_list, name='card-list'),
]
