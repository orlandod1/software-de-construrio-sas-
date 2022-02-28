from django.urls import path
from apps.proovedor.views import indexProovedores,agregarProovedor,ProovedorDelete

from django.contrib.auth.decorators import login_required
app_name="proovedores"

urlpatterns=[
    path('',login_required(indexProovedores),name="indexProovedores"),
    path('agregarProovedor/',login_required(agregarProovedor),name="agregarProovedor"),
    path('eliminar/<int:pk>/', login_required(ProovedorDelete.as_view()), name='proovedor_eliminar'),

    
]