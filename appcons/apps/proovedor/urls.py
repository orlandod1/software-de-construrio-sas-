from django.urls import path
from apps.proovedor.views import indexProovedores,agregarProovedor,proovedorEdit, proovedorEliminar

from django.contrib.auth.decorators import login_required
app_name="proovedores"

urlpatterns=[
    path('',login_required(indexProovedores),name="indexProovedores"),
    path('agregarProovedor/',login_required(agregarProovedor),name="agregarProovedor"),
    path('actualizar/<int:id_proovedor>/',login_required(proovedorEdit), name='proovedorEdit'),
    path('eliminar/<int:id_proovedor>/',login_required(proovedorEliminar), name='proovedorEliminar'), 
    
]