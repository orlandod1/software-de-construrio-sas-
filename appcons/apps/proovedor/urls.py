from django.urls import path
from apps.proovedor.views import indexProovedores,agregarProovedor, proovedorDelete,proovedorEdit

from django.contrib.auth.decorators import login_required
app_name="proovedores"

urlpatterns=[
    path('',login_required(indexProovedores),name="indexProovedores"),
    path('agregarProovedor/',login_required(agregarProovedor),name="agregarProovedor"),
    path('actualizar/<int:id_proovedor>/',login_required(proovedorEdit), name='proovedorEdit'),
    path('eliminar/<int:id>/',login_required(proovedorDelete), name='proovedor_eliminar'), 
    
]