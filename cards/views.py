# cards/views.py
from django.shortcuts import render
from .models import BusinessCard

def card_list(request):
    cards = BusinessCard.objects.all()
    return render(request, "cards/card_list.html", {"cards": cards})
