from django.urls import path
from apps.compra.views import RegistroUsuario, compraDelete, indexCompra,CrearCompra, nuevaCompra, CompraUpdate
from django.contrib.auth.decorators import login_required
app_name = 'compras'

urlpatterns =[
    path('', login_required(indexCompra), name='indexCompra'),
    path('nueva/',login_required(nuevaCompra),name='nuevaCompra'),
    path('nuevacompra/',login_required(CrearCompra.as_view()),name='CrearCompra'),
    path('actualizar/<int:pk>/',login_required( CompraUpdate.as_view()), name='compra_editar'),
    path('eliminar-compra/<int:id>/', login_required(compraDelete), name='compra_delete'),
    path('registro/', (RegistroUsuario.as_view()), name='registro')
  
]