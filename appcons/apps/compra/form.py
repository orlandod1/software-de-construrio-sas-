
from django import forms
from apps.compra.models import Compra
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class DateInput(forms.DateInput):
    input_type = 'date'


#ESTA ES PARA CARGAR EL FORMULARIO DE DJANGO

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'password1', 
            'password2',
            'first_name',
            'last_name',
            'email'
        ]
        labels = {
            'username':'Nombre de usuario',
            'first_name':'Nombres',
            'password1':'Contraseña',
            'password2':'Confirmar contraseña',
            'last_name':' Apellidos',
            'email':'Correo electronico'
        }

        widgets={
            'username': forms.TextInput(attrs={'class':'form-control ','required':'true',}),
            'password1': forms.PasswordInput(attrs={'class':'form-control','required':'true'}),
            'password2': forms.PasswordInput(attrs={'class':'form-control','required':'true'}),
            'first_name': forms.TextInput(attrs={'class':'form-control','required':'true'}),
            'last_name': forms.TextInput(attrs={'class':'form-control','required':'true'}),
            'email': forms.EmailInput(attrs={'class':'form-control','required':'true'}),
        }
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
            'co_fechaIngreso':DateInput(attrs={'class':'form-control'}, format='%Y-%m-%d'),
            'co_Total':forms.NumberInput(attrs={'class':'form-control','readonly':'readonly'}),
        }