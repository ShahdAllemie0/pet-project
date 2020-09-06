from django.db import models


class Pet(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    available = models.BooleanField(default = True,null=True,blank=True)
    image = models.ImageField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
