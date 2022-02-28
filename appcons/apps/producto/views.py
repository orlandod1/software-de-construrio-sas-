from unittest import result
from django.shortcuts import redirect, render
from apps.material.models import Material
from apps.producto.models import Producto
from apps.producto.form import ProductosForm
from django.db.models import Q


# Create your views here.
def indexProducto(request):
    productos = Producto.objects.all().order_by('-id')
    materiales = Material.objects.all()
    context = {'productos':productos,'materiales':materiales}
   
    if request.user.is_authenticated:
        return render(request,'productos/index.html',context)
    else: 
        return redirect('login')



def buscarProducto(request):
   busqueda = request.POST.get("buscar")
  
   productos= Producto.objects.all()

   if busqueda:
        productos= Producto.objects.filter(
            Q(nombre__icontains = busqueda)
   
       
   ).distinct()
  
   context = {'productos':productos}
 
   return render(request,'productos/index.html',context)



def productoEdit (request, id_product):

    producto = Producto.objects.get(pk=id_product)
    if request.method == 'GET':
        form = ProductosForm(instance=producto)
    else:
        form = ProductosForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
        return redirect('productos:productos')

    return render(request,'productos/productosForm.html', {'form':form})  





# class ProductoUpdate(UpdateView):
#     model= Producto
#     second_model = Compra
#     template_name = 'productos/productosForm.html'
#     form_class = ProductosForm
#     second_form_class = ComprasForm
#     success_url = reverse_lazy('productos:indexProducto')

#     def get_context_data(self, **kwargs):
#         context = super(ProductoUpdate,self).get_context_data(**kwargs)
#         pk = self.kwargs.get('pk',0)
#         producto = self.model.objects.get(id =pk)
        
       
        
#         if 'form' not in context:
#             context['form'] = self.form_class=Compra.objects.get(compra=Compra.co_fechaIngreso)

#         if 'form2' not in context:
#             context['form2'] = self.second_form_class=Producto.objects.filter(compra=compra.id)

        
#         context['id'] =pk
#         print (str(compra))
#         return context

# def post(self,request,*args,**kwargs):# para guardar
#     self.object = self.get_object
#     pk = self.kwargs.get('pk',0)
#     compra = self.model.objects.get(id=pk)
#     form = self.form_class(self.request.POST,instance=compra)#trean el reguistro existente
#     productosFormSet= formset_factory(ProductosForm)
#     form2 =  productosFormSet(self.request.POST)
#     if(form.is_valid() and form2.is_valid()):
#         return self.form_valid(form, form2)
#     else:
#         return self.render_to_response(self.get_context_data(form=form, form2 = form2))
            
    
# def form_valid(self, form, form2):
#     self.compra = form.save()
#     form2.instance = self.compra
#     print( form2.instance)  

#     for f in form2:
#         #producto = f.save(commit=False)#se hace un guardado falso
#         #producto.compra = compra#se le asigna el id de la compra a todos los productos
#         p=Producto.objects.get(compra=self.compra)
#         f.intance=p
#         f.save()# se guarda esa uno por uno esos productos
#         print(f.cleaned_data['pro_total'], p.compra)

#     return HttpResponseRedirect(self.get_success_url()) 