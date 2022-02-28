
from logging import PlaceHolder
from operator import imod
from tkinter import Widget
from django import forms
from apps.producto.models import Producto
# from django.contrib.admin.widgets import AutocompleteSelect
# from django.contrib import admin
class ProductosForm(forms.ModelForm):
    class Meta:
        model=Producto

        fields=[
            'nombre',   
            'compra',
            'unidad',
            'pro_cantidad',
            'pro_precio',
            'pro_total',
            'prov_id',

        ]

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
            'compra':forms.Select(attrs={'class':'form-control select2','required': 'true'}),
            'nombre':forms.Select(attrs={'class':'form-control select2','required': 'true'}),
            'prov_id':forms.Select(attrs={'class':'form-control select2','required': 'true'}),
            'unidad':forms.Select(attrs={'class':'form-control select2','required': 'true'}),
            'pro_precio':forms.NumberInput(attrs={'class':'form-control','required': 'true'}),
            'pro_cantidad':forms.NumberInput(attrs={'class':'form-control','required': 'true'}),
            'pro_total':forms.NumberInput(attrs={'class':'form-control','required': 'true'}),
            
        }
    # UNA MEJOR FORMA PARA TRAER LOS WIDGETS Y TRABAJAR CON LOS ATRIBUTOS, AQUI SE ESTÁN DECLARANDO
    #  LOS QUE SON SELECT EN SELECT2 PARA LLAMARLOS EN EL SCRIPT DEL FORMCOMPRAS
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args,**kwargs)
    #     self.fields['prov_id'].widget.attrs.update({
    #                 'class':' form-control select2',
    #                 'required': True}) ,    
    #     self.fields['nombre'].widget.attrs.update({
    #                 'class':' form-control select2',
    #                 'required': True })  
    #     self.fields['unidad'].widget.attrs.update({
    #                 'class':' form-control select2',
    #                 'required': True })    
    #     self.fields['pro_cantidad'].widget.attrs.update({
    #                 'class':' form-control',
    #                 'required': True })    
    #     self.fields['pro_precio'].widget.attrs.update({
    #                 'class':' form-control',
    #                 'required': True })                                            
    #     self.fields['pro_total'].widget.attrs.update({
    #                 'class':' form-control',
    #                 'required': True })    










         # # esta llave foranea de materiales que quiero listar
            # 'nombre':AutocompleteSelect(Producto._meta.get_field('nombre').remote_field,admin.site ,attrs={'class':'form-control','placeholder':'seleccionar el producto' }),