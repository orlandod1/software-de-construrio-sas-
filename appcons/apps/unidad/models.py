from django.db import models

# Create your models here.
class Unidad(models.Model):    
    un_nombre = models.CharField(max_length=10,verbose_name="Unidad")

    def __str__(self):
        return self.un_nombre    

