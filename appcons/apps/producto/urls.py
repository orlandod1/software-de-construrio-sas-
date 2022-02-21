from django.urls import path
from apps.producto.views import indexProducto,buscarProducto, productoEdit
from django.contrib.auth.decorators import login_required
app_name = 'productos'

urlpatterns =[
    path('', login_required(indexProducto), name='indexProducto'),
    path('buscarProducto/',login_required(buscarProducto),name='buscarProducto'),
    path('actualizarp/<int:id_product>/', login_required(productoEdit), name='producto_editar')
]