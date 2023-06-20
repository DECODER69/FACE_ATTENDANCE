from django.db import models

# Create your models here.

class accuracy(models.Model):
    number = models.CharField(max_length=3)
    create = models.CharField(max_length=100, default='')