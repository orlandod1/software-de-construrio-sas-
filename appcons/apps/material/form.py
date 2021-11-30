from django import forms
from apps.material.models import Material

class MaterialFroms(forms.ModelForm):
    class Meta:
        model = Material
        fields=['ma_nombre']

        labels={
            'ma_nombre':'Ingrese el nombre del material'
        }

        widgets={
            'ma_nombre': forms.TextInput(attrs={'class':'form-control'})
        }
