from django.shortcuts import redirect, render
from apps.material.models import Material
from django.contrib.auth.decorators import login_required, permission_required
from apps.material.form import MaterialFroms
# Create your views here.



def indexMateriales(request):
    materiales = Material.objects.all().order_by('-id')#se traen los objetos
    context={'materiales':materiales}#se convierte en diccionario y se le pasa al contexto
    if request.user.is_authenticated:
        return render(request,'materiales/index.html',context)
    else: 
        return redirect('login')


    

def agregarMaterial(request):
    if(request.method == 'POST'):
        form = MaterialFroms(request.POST)
        if(form.is_valid()):
            form.save()
        return redirect('materiales:indexMateriales')
    else:
        form= MaterialFroms()
    return render(request,'materiales/formMateriales.html',{'form':form})

