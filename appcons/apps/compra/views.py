from django.core.files.base import ContentFile
from django.db.models.query import QuerySet
from django.forms.formsets import formset_factory
from django.forms import modelformset_factory,inlineformset_factory
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from apps.compra.models import Compra
from apps.compra.form import ComprasForm
from django.urls import reverse_lazy
from django.views.generic import CreateView,UpdateView

from apps.producto.views import indexProducto
from apps.producto.form import ProductosForm
from apps.producto.models import Producto



# Create your views here.
def indexCompra(request):
    compras = Compra.objects.all().order_by('-id')
    context = {'compras':compras}
    return render(request,'compras/index.html',context)


def nuevaCompra(request):
    ProductoFormSet= formset_factory(ProductosForm)#lo que hace es poder crear varias instacias del form
    if request.method == 'POST':
        form2=ProductoFormSet(request.POST,request.FILES)
        form=ComprasForm(request.POST,request.FILES)
        if form2.is_valid() and form.is_valid():
            compra = form.save(commit=False)#se hace un guardado falso
            compra.co_Total=0
            for f2 in form2:#se guarda el costo total de la compra respecto alos produtos
                producto1 = f2.save(commit=False)#se hace un guardado falso
                producto1.pro_total=producto1.pro_cantidad*producto1.pro_precio
                compra.co_Total+=producto1.pro_total
                
            compra.save()# se guarda esa compra
            for f in form2:
                producto = f.save(commit=False)#se hace un guardado falso
                producto.compra = compra#se le asigna el id de la compra a todos los productos
                producto.save()# se guarda esa uno por uno esos productos
            return redirect('productos:indexProducto')#se redirecciona al index de producto
    else:
        form2 = ProductoFormSet()#en la primera pasada mandamos a renderizar los formularios
        form = ComprasForm()#en la vista 

    return render(request,'compras/formCompras.html',{'form':form,'form2':form2 })

class CrearCompra(CreateView):
    model = Compra#modelo principal
    template_name = 'compras/formCompras.html'#vista del template
    form_class =  ComprasForm
    second_form_class = formset_factory(ProductosForm)
    success_url = reverse_lazy('compras:indexCompra')

    def get_context_data(self, **kwargs):#se valida el contexto y si no se anda por parametro
        context = super(CrearCompra,self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)#se traen todos los formularios
        if 'form2' not in context:
            context['form2'] = self.second_form_class()

        return context

    def post(self,request,*args,**kwargs):# para guardar
        self.object = self.get_object
        form = self.form_class(request.POST)
        form2 =  self.second_form_class(request.POST)

        if form.is_valid() and form2.is_valid():
            compra = form.save(commit=False)#se hace un guardado falso
            compra.co_Total=0
            for f2 in form2:#se guarda el costo total de la compra respecto alos produtos
                producto1 = f2.save(commit=False)#se hace un guardado falso
                producto1.pro_total=producto1.pro_cantidad*producto1.pro_precio
                compra.co_Total+=producto1.pro_total
                
            compra.save()# se guarda esa compra
            for f in form2:
                producto = f.save(commit=False)#se hace un guardado falso
                producto.compra = compra#se le asigna el id de la compra a todos los productos
                producto.save()# se guarda esa uno por uno esos productos
           
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form, form2 = form2))
            

class compraUpdate(UpdateView):
    model = Compra
    second_model = Producto
    template_name = 'compras/formCompras.html'
    form_class = ComprasForm
    second_form_class = modelformset_factory(Producto,ProductosForm,extra=0)
    #second_form_class = inlineformset_factory(Compra,Producto,ProductosForm,extra=0)
    
    success_url = reverse_lazy('compras:indexCompra')

    def get_context_data(self, **kwargs):
        #self.object = Compra.objects.get(pk=self.request.compra.id)
        context = super(compraUpdate,self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk',0)
        compra = self.model.objects.get(id=pk)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(queryset=Producto.objects.filter(compra=compra.id))
            #context['form2'] = self.second_form_class(instance=compra)
        context['id'] = pk
        return context

    
    def post(self,request,*args,**kwargs):# para guardar
        self.object = self.get_object
        pk = self.kwargs.get('pk',0)
        compra = self.model.objects.get(id=pk)
        form = self.form_class(self.request.POST,instance=compra)#trean el reguistro existente
        productosFormSet= formset_factory(ProductosForm)
        form2 =  productosFormSet(self.request.POST)
        if(form.is_valid() and form2.is_valid()):
            return self.form_valid(form, form2)
        else:
            return self.render_to_response(self.get_context_data(form=form, form2 = form2))
            
    
    def form_valid(self, form, form2):
        self.compra = form.save()
        form2.instance = self.compra
        print( form2.instance)

        for f in form2:
            #producto = f.save(commit=False)#se hace un guardado falso
            #producto.compra = compra#se le asigna el id de la compra a todos los productos
            p=Producto.objects.get(compra=self.compra)
            f.intance=p
            f.save()# se guarda esa uno por uno esos productos
            print(f.cleaned_data['pro_total'], p.compra)

        return HttpResponseRedirect(self.get_success_url())

#Se trae la compra 
#Se instacia esa compra en un form
#Se buscan todos los productos de esa compra
##################################
#Se arma una instacia de todos esos productos ---
#Se actualiza la compra<-----
#Se pueda agregar un nuevo producto o editar los existentes xxxxxxxxxx
#Se actulicen los que ya existen y se creen los nuevos xxxxxxxxxxxx