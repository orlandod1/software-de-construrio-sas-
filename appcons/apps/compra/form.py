from django import forms
from apps.compra.models import Compra

class DateInput(forms.DateInput):
    input_type = 'date'
    

class ComprasForm(forms.ModelForm):
    class Meta:
        model=Compra

        fields={
            'co_fechaIngreso',
            'co_Total',
        }

        labels={
            'co_fechaIngreso':'fecha de la compra',
            'co_Total':'Costo total'
            
        }

        widgets={
            'co_fechaIngreso':DateInput(attrs={'class':'form-control'}),
            'co_Total':forms.NumberInput(attrs={'class':'form-control'}),
        }