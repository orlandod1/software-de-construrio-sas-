from django import forms
from django.forms import formset_factory
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from apps.material.models import Material
from apps.material.form import MaterialFroms


class FormSetMaterial(FormView):
   
    
    
    
    template_name="materiales/formMateriales.html"
    form_class= formset_factory(MaterialFroms,extra=1)
    success_url = reverse_lazy('materiales:indexMateriales')



    def form_valid(self, form):
        ##print(form)
        for f in form:
            if f.is_valid():
                print(f.cleaned_data['ma_nombre'])
                m= f.save(commit=False)#no reguistro en la base de datos hasta que se confirme
                m.save()

              
        return super().form_valid(form)





   