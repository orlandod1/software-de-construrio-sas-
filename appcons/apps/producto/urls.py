from django.urls import path
from apps.producto.views import indexProducto,buscarProducto

app_name = 'productos'

urlpatterns =[
    path('', indexProducto, name='indexProducto'),
    path('burcarProducto/',buscarProducto,name='buscarProducto')
]