from django.urls import path
from apps.producto.views import indexProducto,nuevoProducto

app_name = 'productos'

urlpatterns =[
    path('', indexProducto, name='indexProducto'),
    path('nuevoproducto/',nuevoProducto,name='nuevoProducto')
]