from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from apps.unidad.forms import  UnidadForms
from apps.unidad.models import Unidad


from django.views.generic import DeleteView
# Create your views here.



def indexUnidades(request):
    unidades = Unidad.objects.all().order_by('-id')#se traen los objetos
    context={'unidades':unidades}#se convierte en diccionario y se le pasa al contexto
    if request.user.is_authenticated:
        return render(request,'unidades/index.html',context)
    else: 
        return redirect('login')


    

def agregarUnidad(request):
    if(request.method == 'POST'):
        form = UnidadForms(request.POST)
        if(form.is_valid()):
            form.save()
        return redirect('unidades:indexUnidades')
    else:
        form= UnidadForms()
    return render(request,'unidades/formUnidades.html',{'form':form})

class UnidadDelete(DeleteView):
    model= Unidad
    template_name= 'unidades/unidaddelete.html'
    success_url = reverse_lazy('unidades:indexUnidades')