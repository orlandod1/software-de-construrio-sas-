from django.shortcuts import redirect, render
from apps.material.models import Material
from apps.producto.models import Producto
from apps.producto.form import ProductosForm


# Create your views here.
def indexProducto(request):
    productos = Producto.objects.all().order_by('-id')
    context = {'productos':productos}
    return render(request,'productos/index.html',context)

def buscarProducto(request):
   termino = request.GET['termino']
   material = Material.objects.get(ma_nombre=termino)
   productos = Producto.objects.filter(nombre=material.id)
   context = {'productos':productos}
   return render(request,'productos/index.html',context)