from django.db import models
from django.forms import model_to_dict

# Create your models here.

class Material(models.Model):
    ma_nombre = models.CharField(null=False,blank=False,max_length=50,verbose_name="Nombre del material")

    # def __str__(self) -> str:
    #     return self.ma_nombre  

    
    def toJSON(self):
        item= model_to_dict(self)
        #item['ma_compra']=self.ma_nombre.toJSON
        return item

  
