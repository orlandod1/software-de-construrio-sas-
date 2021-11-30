from django.db import models
from django.db.models.base import Model


# Create your models here.
class Proyecto (models.Model):
    pro_nombre= models.CharField(max_length=20,verbose_name="Nombre del proyecto")
    pro_fechainicio= models.DateField(verbose_name="Fecha de creación")
    pro_fechafinal= models.DateField(verbose_name="Fecha de terminación")
    pro_presupuesto= models.IntegerField(max_length=11,verbose_name="presupuesto")
    pro_costo= models.PositiveIntegerField(max_length=11,verbose_name="Costo")
    pro_gasto= models.PositiveIntegerField(max_length=11,verbose_name="Gasto")
    

    def __str__(self):
        return  '{}'.format(self.pro_nombre)


    class Meta:
        verbose_name="Proyecto"
        verbose_name_plural="Proyectos"
    
