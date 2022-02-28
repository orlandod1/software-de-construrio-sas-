from django import forms
from apps.proovedor.models import Proovedor

class ProovedorForms(forms.ModelForm):
    class Meta:
        model = Proovedor
        fields=['proov_nombre','proov_dni']

        labels={
            'proov_nombre':'Ingrese el nombre del proovedor',
            'proov_dni':'DNI del proovedor'
        }

        widgets={
            'proov_nombre': forms.TextInput(attrs={'class':'form-control','required':'true'}),
            'proov_dni': forms.NumberInput(attrs={'class':'form-control','required':'true'}),

        }
