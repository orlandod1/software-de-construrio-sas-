from django.db import models
from django.db.models.base import Model



# Create your models here.
class Compra (models.Model):
    co_fechaIngreso= models.DateField()
    co_Total= models.PositiveIntegerField(max_length=11,verbose_name="Total")
    
    

    def __str__(self):
        return  '{}'.format(self.co_fechaIngreso)


    class Meta:
        verbose_name="Compra"
        verbose_name_plural="Compras"
    

    

