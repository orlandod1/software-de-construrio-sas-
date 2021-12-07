
from django import forms
from apps.producto.models import Producto

class ProductosForm(forms.ModelForm):
    class Meta:
        model=Producto

        fields={
            'nombre',
            'compra',
            'unidad',
            'pro_cantidad',
            'pro_precio',
            'pro_total',
            'prov_id',

        }

        labels={
            'nombre':'Nombre del producto',
            'compra':'Compra',
            'unidad':'Unidad',
            'pro_cantidad':'Cantidad',
            'pro_precio':'Precio',
            'pro_total':'Total',
            'prov_id':'proovedor',
        }

        widgets={
            'nombre':forms.Select(attrs={'class':'form-control','required':'true'}),
            'compra':forms.Select(attrs={'class':'form-control','required':'true'}),
            'unidad':forms.Select(attrs={'class':'form-control','required':'true'}),
            'pro_cantidad':forms.NumberInput(attrs={'class':'form-control','required':'true'}),
            'pro_precio':forms.NumberInput(attrs={'class':'form-control','required':'true'}),
            'pro_total':forms.NumberInput(attrs={'class':'form-control','readonly':'readonly'}),
            'prov_id':forms.Select(attrs={'class':'form-control','required':'true'}),
        
        }