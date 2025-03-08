from django.db import models

class Post(models.Model):
    PET_VALUES = [
        ('1', 'собака'),
        ('2', 'кошка'),
    ]

    name = models.CharField(max_length=255)
    text = models.TextField()
    pet = models.CharField(max_length=1, choices=PET_VALUES)
