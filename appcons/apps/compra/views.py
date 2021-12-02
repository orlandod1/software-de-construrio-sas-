from django.core.files.base import ContentFile
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from apps.compra.models import Compra
from apps.compra.form import ComprasForm
from apps.producto.views import indexProducto
from apps.producto.form import ProductosForm
from apps.producto.models import Producto
from django.urls import reverse_lazy
from django.views.generic import CreateView    


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



class CrearCompra(CreateView):
    model = Compra
    
    template_name = 'compras/formCompras.html'
    form_class =  ComprasForm
    second_form_class = ProductosForm
    success_url = reverse_lazy('compras:indexCompra')

    def get_context_data(self, **kwargs):
        context = super(CrearCompra,self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
            return context

    def post(self,request,*args,**kwargs):

        self.object = self.get_object
        form = self.form_class(request.POST)
        form2 =  self.second_form_class(request.POST)

        if form.is_valid() and form2.is_valid():
            compra = form.save(commit = False)
            compra.Producto = form2.save()  
            compra.save()
            return HttpResponseRedirect(self.get_success_url())

        else:
            return self.render_to_response(self.get_context_data(form=form, form2 = form2))
            