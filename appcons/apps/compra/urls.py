from django.urls import path
from apps.compra.views import indexCompra
app_name = 'compras'

urlpatterns =[
    path('', indexCompra, name='indexCompra'),
]  