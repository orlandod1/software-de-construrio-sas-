from django.core.files.base import ContentFile
from django.forms.formsets import formset_factory
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from apps.compra.models import Compra
from apps.compra.form import ComprasForm
from django.urls import reverse_lazy
from django.views.generic import CreateView  

from apps.producto.views import indexProducto
from apps.producto.form import ProductosForm
from apps.producto.models import Producto



# Create your views here.
def indexCompra(request):
    compras = Compra.objects.all().order_by('-co_fechaIngreso')
    context = {'compras':compras}
    return render(request,'compras/index.html',context)


def nuevaCompra(request):
    ProductoFormSet= formset_factory(ProductosForm)# o que hace es poder crear varias instacias del form
    if request.method == 'POST':
        form2=ProductoFormSet(request.POST,request.FILES)
        form=ComprasForm(request.POST,request.FILES)
        if form2.is_valid() and form.is_valid():
            compra = form.save(commit=False)#se hace un guardado falso
            for f2 in form2:
                producto = f2.save(commit=False)#se hace un guardado falso
                producto.pro_total=producto.pro_cantidad*producto.pro_precio
                compra.co_Total=compra.co_Total+producto.pro_total

            compra.save()
            for f in form2:
                producto = f.save(commit=False)#se hace un guardado falso
                producto.compra = compra#se le asigna 
                producto.pro_total=producto.pro_cantidad*producto.pro_precio
                producto.save()
           


           
            return redirect('productos:indexProducto')
    else:
        form2 = ProductoFormSet()
        form = ComprasForm()

    return render(request,'compras/formCompras.html',{'form':form,'form2':form2 })

class CrearCompra(CreateView):
    model = Compra#modelo principal
    template_name = 'compras/formCompras.html'#vista del template
    form_class =  ComprasForm
    second_form_class = ProductosForm
    success_url = reverse_lazy('compras:indexCompra')

    def get_context_data(self, **kwargs):#se valida el contexto y si no se anda por parametro
        context = super(CrearCompra,self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)#se traen todos los formularios
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
            
        return context

    def post(self,request,*args,**kwargs):# para guardar
        self.object = self.get_object
        form = self.form_class(request.POST)
        form2 =  self.second_form_class(request.POST)

        if form.is_valid() and form2.is_valid():
            compra = form.save(commit = False)#se hace un guardado falso
            producto = form2.save(commit=False)#se hace un guardado falso
            producto.compra = compra#se le asigna 
            producto.pro_total=producto.pro_cantidad*producto.pro_precio
            compra.save()
            producto.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form, form2 = form2))
            