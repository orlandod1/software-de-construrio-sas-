from django.contrib import admin

from apps.producto.models import Producto

# Register your models here.
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre','compra','unidad','pro_cantidad','pro_precio','pro_total','prov_id')
    autocomplete_fields =('nombre','prov_id')


admin.site.register(Producto,ProductoAdmin)

