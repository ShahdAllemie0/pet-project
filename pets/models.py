from django.db import models
from django.urls import reverse


class Pet(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    available = models.BooleanField(default = True,null=True,blank=True)
    image = models.ImageField(null=True,blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pet_id':self.id})
