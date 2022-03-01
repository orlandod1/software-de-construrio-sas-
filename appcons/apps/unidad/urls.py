from django.urls import path
from apps.unidad.views import indexUnidades,agregarUnidad, unidadDelete, unidadEdit

from django.contrib.auth.decorators import login_required
app_name="unidades"

urlpatterns=[
    path('',login_required(indexUnidades),name="indexUnidades"),
    path('agregarUnidad/',login_required(agregarUnidad),name="agregarUnidad"),
      path('actualizar/<int:id_unidad>/',login_required(unidadEdit), name='unidadEdit'),
    path('eliminar/<int:id>/',login_required(unidadDelete), name='unidadDelete')

    
]