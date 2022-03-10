from django import forms
from apps.material.models import Material
from django.forms import Form, ValidationError

class MaterialFroms(forms.ModelForm):


    #VALIDACION OJO!! LA FUNCION CLEAR DEBE TENER SEGUIDO EL ATRIBUTO DE X O Y MODELO A UTILIZAR
    def clean_ma_nombre(self):
        ma_nombre = self.cleaned_data["ma_nombre"]
        
        existe= Material.objects.filter(ma_nombre__iexact=ma_nombre).exists()
        
        if existe:
            raise ValidationError("Este material ya existe")
        
        return ma_nombre             
    
    class Meta:
        model = Material
        fields=['ma_nombre','id']

        labels={
            'ma_nombre':'Ingrese el nombre del material'
        }

        
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.fields['ma_nombre'].widget.attrs.update({
                    'class':' form-control',
                    'required': True}) 