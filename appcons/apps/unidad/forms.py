from django import forms
from apps.unidad.models import Unidad

class UnidadForms(forms.ModelForm):
    class Meta:
        model = Unidad
        fields=['un_nombre']

        labels={
            'un_nombre':'Ingrese la unidad',
           
        }

        widgets={
            'un_nombre': forms.TextInput(attrs={'class':'form-control','required':'true'}),
           

        }
