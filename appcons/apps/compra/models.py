from django.db import models
from django.db.models.base import Model

# Create your models here.
class Compra (models.Model):

    co_cantidad = models.IntegerField(max_length=11,verbose_name="Cantidad")


    