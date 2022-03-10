from django import forms
from apps.unidad.models import Unidad

class UnidadForms(forms.ModelForm):
    
    
    
    
    def clean_nombrematerial(self):
        un_nombre = self.cleaned_data.GET("un_nombre")
        existe= Unidad.objects.filter(un_nombre=un_nombre).exists()
            
        if existe:
            raise forms.ValidationError("Esta unidad ya existe")

        return un_nombre     
          
    class Meta:
        model = Unidad
        fields=['un_nombre']

        labels={
            'un_nombre':'Ingrese la unidad',
           
        }

        widgets={
            'un_nombre': forms.TextInput(attrs={'class':'form-control','required':'true'}),
           

        }
