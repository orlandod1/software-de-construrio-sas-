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
            'co_fechaIngreso':'Fecha de la compra',
            'co_Total':'Costo total'
            
        }

        widgets={
            'co_fechaIngreso':DateInput(attrs={'class':'form-control','pattern':'[0-9]{4}-[0-9]{2}-[0-9]{2}'}),
            'co_Total':forms.NumberInput(attrs={'class':'form-control','readonly':'readonly'}),
        }