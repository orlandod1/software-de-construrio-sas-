from django.db import models
from apps.material.models import Material
from apps.unidad.models import Unidad
from apps.compra.models import Compra
from apps.proovedor.models import Proovedor

# Create your models here.

class Producto  (models.Model):
    nombre= models.ForeignKey(Material,null=True,blank=True,on_delete=models.CASCADE)
    compra = models.ForeignKey(Compra,null=True,blank=True,on_delete=models.CASCADE)
    unidad = models.ForeignKey(Unidad,null=True,blank=True,on_delete=models.CASCADE)
    pro_cantidad = models.PositiveIntegerField(max_length=10, verbose_name="Cantidad")
    pro_precio = models.PositiveIntegerField(max_length=10, verbose_name="Precio")
    pro_total = models.PositiveIntegerField(max_length=10, verbose_name="Total")
    prov_id= models.ForeignKey(Proovedor,null=True,blank=True,on_delete=models.CASCADE,verbose_name="Provedor")
   


    class Meta:
        verbose_name ="Producto"
        verbose_name_plural ="Productos"


