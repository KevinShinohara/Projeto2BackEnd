from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

class Movies(models.Model):
    title = models.CharField(max_length=200)
    rating = models.PositiveIntegerField(null=True, blank=True, default=None, validators=[MinValueValidator(1), MaxValueValidator(5)])
