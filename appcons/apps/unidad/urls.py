from django.urls import path
from apps.unidad.views import indexUnidades,agregarUnidad, unidadEdit, unidadEliminar

from django.contrib.auth.decorators import login_required
app_name="unidades"

urlpatterns=[
    path('',login_required(indexUnidades),name="indexUnidades"),
    path('agregarUnidad/',login_required(agregarUnidad),name="agregarUnidad"),
      path('actualizar/<int:id_unidad>/',login_required(unidadEdit), name='unidadEdit'),
    path('eliminar/<int:id_unidad>/',login_required(unidadEliminar), name='unidadEliminar')

    
]