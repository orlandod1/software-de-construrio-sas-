from django.shortcuts import render
from apps.compra.models import Compra
# Create your views here.
def indexCompra(request):
    compras = Compra.objects.all().order_by('co_fechaIngreso')
    context = {'compras':compras}
    return render(request,'compras/index.html',context)



