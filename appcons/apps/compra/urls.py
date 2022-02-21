from django.urls import path
from apps.compra.views import ComprasDelete, RegistroUsuario, indexCompra,CrearCompra, nuevaCompra, CompraUpdate
from django.contrib.auth.decorators import login_required
app_name = 'compras'

urlpatterns =[
    path('', login_required(indexCompra), name='indexCompra'),
    path('nueva/',login_required(nuevaCompra),name='nuevaCompra'),
    path('nuevacompra/',login_required(CrearCompra.as_view()),name='CrearCompra'),
    path('actualizar/<int:pk>/',login_required( CompraUpdate.as_view()), name='compra_editar'),
    path('eliminar/<int:pk>/', login_required(ComprasDelete.as_view()), name='compra_eliminar'),
    path('registro/', (RegistroUsuario.as_view()), name='registro')
  
]