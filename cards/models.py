# cards/models.py
from django.db import models

class BusinessCard(models.Model):
    name = models.CharField(max_length=255)  # optional
    front_image = models.ImageField(upload_to='cards/')
    back_image = models.ImageField(upload_to='cards/')

    def __str__(self):
        return self.name or f'Card {self.pk}'
