from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from apps.proovedor.forms import ProovedorForms
from apps.proovedor.models import Proovedor
from django.contrib.auth.decorators import login_required, permission_required

from django.views.generic import DeleteView
# Create your views here.



def indexProovedores(request):
    proovedores = Proovedor.objects.all().order_by('-id')#se traen los objetos
    context={'proovedores':proovedores}#se convierte en diccionario y se le pasa al contexto
    if request.user.is_authenticated:
        return render(request,'proovedores/index.html',context)
    else: 
        return redirect('login')


    

def agregarProovedor(request):
    if(request.method == 'POST'):
        form = ProovedorForms(request.POST)
        if(form.is_valid()):
            form.save()
        return redirect('proovedores:indexProovedores')
    else:
        form= ProovedorForms()
    return render(request,'proovedores/formProovedores.html',{'form':form})

class ProovedorDelete(DeleteView):
    model= Proovedor
    template_name= 'proovedores/proovedordelete.html'
    success_url = reverse_lazy('proovedores:indexProovedores')



def proovedorDelete(request,id):
    proovedor = Proovedor.objects.get(id=id)
    proovedor.delete()

    return redirect('proovedores:indexProovedores')
  
 


def proovedorEdit (request, id_proovedor):

    proovedor = Proovedor.objects.get(pk=id_proovedor)
    if request.method == 'GET':
        form = ProovedorForms(instance=proovedor)
    else:
        form = ProovedorForms(request.POST, instance=proovedor)
        if form.is_valid():
            form.save()
        return redirect('proovedores:indexProovedores')

    return render(request,'proovedores/formProovedores.html', {'form':form})                      
