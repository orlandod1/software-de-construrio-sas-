from django.db import models

# Create your models here.

class Material(models.Model):
    ma_nombre = models.CharField(null=False,blank=False,max_length=50,verbose_name="Nombre del material")

    def __str__(self) -> str:
        return self.ma_nombre  

  
