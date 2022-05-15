from django.db import models

# Create your models here.

class Product(models.Model):
    name=models.CharField(max_length=50)
    date_production=models.DateField()
    made_in=models.CharField(max_length=50)
    qte=models.IntegerField()
    price=models.IntegerField()

    class Meta:
        ordering=('name')
