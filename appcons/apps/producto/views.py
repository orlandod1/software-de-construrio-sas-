from django.shortcuts import redirect, render
from apps.producto.models import Producto
from apps.producto.form import ProductosForm


# Create your views here.
def indexProducto(request):
    productos = Producto.objects.all().order_by('-id')
    context = {'productos':productos}
    return render(request,'productos/index.html',context)


def nuevoProducto(request):
    if(request.method == 'POST'):
        form = ProductosForm(request.POST)
        if(form.is_valid()):
            form.save()
        return redirect('productos:indexProducto')
    else:
        form= ProductosForm()
    return render(request,'productos/ProductosForm.html',{'form':form})