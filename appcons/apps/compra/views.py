from django.shortcuts import redirect, render
from apps.compra.models import Compra
from apps.compra.form import ComprasForm

# Create your views here.
def indexCompra(request):
    compras = Compra.objects.all().order_by('-co_fechaIngreso')
    context = {'compras':compras}
    return render(request,'compras/index.html',context)


def nuevaCompra(request):
    if(request.method == 'POST'):
        form = ComprasForm(request.POST)
        if(form.is_valid()):
            form.save()
        return redirect('compras:indexCompra')
    else:
        form= ComprasForm()
    return render(request,'compras/formCompras.html',{'form':form})