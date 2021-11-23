from django.db import models

# Create your models here.
class Proovedor(models.Model):

    proov_nombre = models.CharField(max_length=30,verbose_name="Nombre del proovedor")
    proov_dni = models.IntegerField (max_length=15,verbose_name="Dni del proovedor")

    def __str__(self):
        return self.proov_nombre


    class Meta:
        verbose_name ="Proovedor"
        verbose_name ="Proovedores"    