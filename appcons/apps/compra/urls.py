from django.urls import path
from apps.compra.views import indexCompra,nuevaCompra

app_name = 'compras'

urlpatterns =[
    path('', indexCompra, name='indexCompra'),
    path('nueva/',nuevaCompra,name='nuevaCompra')
]