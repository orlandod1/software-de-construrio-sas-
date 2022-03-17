from cmath import e
import json
from multiprocessing import context
from django.contrib import messages
from django.forms.formsets import formset_factory
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from apps.compra.form import ComprasForm, CustomUserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView ,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from apps.producto.form import ProductosForm
from apps.producto.models import Producto
from django.contrib.auth.models import User
from apps.material.models import Material
from apps.compra.models import Compra

# Create your views here.
def indexCompra(request):
    compras = Compra.objects.all().order_by('-co_fechaIngreso')
    
    context = {'compras':compras}
    if request.user.is_authenticated:
        return render(request,'compras/index.html',context)
    else: 
        return redirect('login')


        
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
            messages.success(request,'¡compra creada con exito!')
            return redirect('compras:indexCompra')#se redirecciona al index de producto
    else:
        productos= Material.objects.all()
        print(productos)
        form2 = ProductoFormSet()#en la primera pasada mandamos a renderizar los formularios
        form = ComprasForm()#en la vista 
       
    return render(request,'compras/formCompras.html',{'form':form,'form2':form2,'productos':productos} )



#VISTA PARA CREAR LA COMPRA POR MEDIO DE VISTA BASADA EN CLASES

# class CrearCompra(CreateView):
#     model = Compra#modelo principal
#     template_name = 'compras/formCompras.html'#vista del template
#     form_class =  ComprasForm
#     second_form_class = formset_factory(ProductosForm)
#     success_url = reverse_lazy('compras:indexCompra')

#     def get_context_data(self, **kwargs):#se valida el contexto y si no se anda por parametro
#         context = super(CrearCompra,self).get_context_data(**kwargs)
#         if 'form' not in context:
#             context['form'] = self.form_class(self.request.GET)#se traen todos los formularios
#         if 'form2' not in context:
#             context['form2'] = self.second_form_class()

#         return context

#     def post(self,request,*args,**kwargs):# para guardar
#         self.object = self.get_object
#         form = self.form_class(request.POST)
#         form2 =  self.second_form_class(request.POST)

#         if form.is_valid() and form2.is_valid():
#             compra = form.save(commit = False)#se hace un guardado falso
#             for producto in form2:
#                 producto = form2.save(commit=False)#se hace un guardado falso
#                 producto.compra = compra#se le asigna 
#                 producto.pro_total=producto.pro_cantidad*producto.pro_precio
#                 producto.save()
                
#             compra.save()
           
#             return HttpResponseRedirect(self.get_success_url())
#         else:
#             return self.render_to_response(self.get_context_data(form=form, form2 = form2))
            


class CompraUpdate(UpdateView):
    model= Compra
    second_model = Producto
    template_name = 'compras/formCompras.html'
    form_class = ComprasForm
    second_form_class = ProductosForm
    success_url = reverse_lazy('compras:indexCompra')

    def get_context_data(self, **kwargs):
        context = super(CompraUpdate,self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk',0)
        compra = self.model.objects.get(id =pk)
        
       
        
        if 'form' not in context:
            context['form'] = self.form_class=Compra.objects.get(compra=Compra.co_fechaIngreso)

        if 'form2' not in context:
            context['form2'] = self.second_form_class=Producto.objects.filter(compra=compra.id)

        
        context['id'] =pk
        print (str(compra))
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


def compraDelete(request,id):
    compra = Compra.objects.get(id=id)
    compra.delete()

    return redirect('compras:indexCompra')
   
   #ESTA FUNCION ES PARA REGISTRAR EL USUARIO

class RegistroUsuario(CreateView):

    model = User 
    template_name = "registration/registro.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('compras:indexCompra')



#########crear compra ########

class CrearCompra(CreateView):
    model = Compra
    form_class = ComprasForm
    template_name = 'compras/Crear_Compras.html'
    success_url = reverse_lazy('compras:indexCompra')   
    url_redirect = success_url 

    @method_decorator(csrf_exempt)
    def dispatch(self, request: HttpRequest, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request: HttpRequest) :
        data = []
        try:
            action = request.POST['action']
            if action == 'search':
                materiales = Material.objects.filter(ma_nombre__contains=request.POST['term'])
                #name__icontains es para omitir mayusculas y minisculas en el termino                
                print(materiales)
                for m in materiales :
                    item=m.toJSON()#convierto el elemento a dicccionario
                    item['text']=item['ma_nombre']#el autocomlete necesita un value para poder funcionar
                    item['value']=item['ma_nombre']
                    print(item)
                    data.append(item)
                   
                    
            else:
                data['error']= 'No se ha ingresado ninguna opcion'
        except Exception as e:
            data['error']= str(e)

        return JsonResponse(data,safe=False)
        #return HttpResponse(json.dumps( data))
    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['title']="Crear una nueva compra"
        context['entity']="compras"
        context['list_url']=self.success_url
        context['action']='add'

        return super().get_context_data(**kwargs)