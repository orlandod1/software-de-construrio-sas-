from django.shortcuts import redirect, render
from apps.material.models import Material
from apps.material.form import MaterialFroms
# Create your views here.


def indexMateriales(request):
    materiales = Material.objects.all().order_by('ma_nombre')#se traen los objetos
    context={'materiales':materiales}#se convierte en diccionario y se le pasa al contexto
    return render(request,'materiales/index.html',context)


def agregarMaterial(request):
    if(request.method == 'POST'):
        form = MaterialFroms(request.POST)
        if(form.is_valid()):
            form.save()
        return redirect('materiales:indexMateriales')
    else:
        form= MaterialFroms()
    return render(request,'materiales/formMateriales.html',{'form':form})
