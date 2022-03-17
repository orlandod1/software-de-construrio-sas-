from ast import Return
from django.db import models
from django.forms import model_to_dict
from apps.material.models import Material
from apps.unidad.models import Unidad
from apps.compra.models import Compra
from apps.proovedor.models import Proovedor

# Create your models here.

class Producto  (models.Model):
    compra = models.ForeignKey(Compra,null=True,blank=True,on_delete=models.CASCADE)
    nombre= models.ForeignKey(Material,null=True,blank=True,on_delete=models.CASCADE)
    unidad = models.ForeignKey(Unidad,null=True,blank=True,on_delete=models.CASCADE)
    pro_cantidad = models.PositiveIntegerField(max_length=10, verbose_name="Cantidad")
    pro_precio = models.PositiveIntegerField(max_length=10, verbose_name="Precio")
    pro_total = models.PositiveIntegerField(max_length=10, verbose_name="Subtotal")
    prov_id= models.ForeignKey(Proovedor,null=True,blank=True,on_delete=models.CASCADE,verbose_name="Provedor")
   


    class Meta:
        verbose_name ="Producto"
        verbose_name_plural ="Productos"


    def toJSON(self):
        item: model_to_dict(self)
        item['compra']=self.compra.toJSON
        item['nombre']=self.nombre.toJSON
        item['unidad']=self.unidad.toJSON
        item['pro_cantidad']=self.pro_cantidad.toJSON
        item['pro_precio']=format(self.pro_precio,'.2f')
        item['pro_total']=format(self.pro_total,'.2f')
        item['prov_id']=self.prov_id.toJSON
        
        return item

