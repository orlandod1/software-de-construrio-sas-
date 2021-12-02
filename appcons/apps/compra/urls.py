from django.urls import path
from apps.compra.views import indexCompra,CrearCompra, nuevaCompra

app_name = 'compras'

urlpatterns =[
    path('', indexCompra, name='indexCompra'),
    path('nueva/',nuevaCompra,name='nuevaCompra'),
    path('nuevacompra/',CrearCompra.as_view(),name='CrearCompra')


]