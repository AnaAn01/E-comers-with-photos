from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=0)
    image = models.ImageField(upload_to='images')
