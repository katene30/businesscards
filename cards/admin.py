# cards/admin.py
from django.contrib import admin
from .models import BusinessCard

@admin.register(BusinessCard)
class BusinessCardAdmin(admin.ModelAdmin):
    list_display = ('name',)
