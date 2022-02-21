from django.contrib import admin
from apps.producto.models import Producto
from apps.compra.models import Compra
# Register your models here.
class MembershipInline(admin.TabularInline):
    model = Producto
    extra = 1
    

class CompraAdmin(admin.ModelAdmin):
    inlines = (MembershipInline,)
    list_display = ('co_fechaIngreso','co_Total')
admin.site.register(Compra,CompraAdmin)