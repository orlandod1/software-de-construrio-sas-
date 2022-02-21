from django.shortcuts import redirect, render
from apps.material.models import Material
from apps.producto.models import Producto
from apps.producto.form import ProductosForm


# Create your views here.
def indexProducto(request):
    productos = Producto.objects.all().order_by('-id')
    materiales = Material.objects.all()
    context = {'productos':productos,'materiales':materiales}
   
    if request.user.is_authenticated:
        return render(request,'productos/index.html',context)
    else: 
        return redirect('login')

def buscarProducto(request):
   termino = request.GET['termino']
   
   productos= Producto.objects.filter(
       nombre=Material.objects.get(ma_nombre__icontains = termino)
   )
   context = {'productos':productos}
 
   return render(request,'productos/index.html',context)



def productoEdit (request, id_product):

    producto = Producto.objects.get(pk=id_product)
    if request.method == 'GET':
        form = ProductosForm(instance=producto)
    else:
        form = ProductosForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
        return redirect('productos:productos')

    return render(request,'productos/productosForm.html', {'form':form})  