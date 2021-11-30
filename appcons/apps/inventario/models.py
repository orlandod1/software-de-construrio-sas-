from django.db import models
from django.db.models.fields import IntegerField

# Create your models here.

class inventario(models.Model):

    in_nombre = models.CharField(max_length=70,verbose_name ='Nombre del material')
    in_costo = models.PositiveIntegerField(max_length=13,verbose_name='Costo total ')
    



