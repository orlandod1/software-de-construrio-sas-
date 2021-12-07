from django.urls import path
from apps.compra.views import indexCompra,CrearCompra, nuevaCompra,compraUpdate

app_name = 'compras'

urlpatterns =[
    path('', indexCompra, name='indexCompra'),
    path('nueva/',nuevaCompra,name='nuevaCompra'),
    path('nuevacompra/',CrearCompra.as_view(),name='CrearCompra'),
    path(r'actualizarcompra/(?P<pk>)\d+)$',compraUpdate.as_view(),name ='compraUpdate')
]