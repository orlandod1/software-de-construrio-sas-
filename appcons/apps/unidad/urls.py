from django.urls import path
from apps.unidad.views import indexUnidades,agregarUnidad,UnidadDelete

from django.contrib.auth.decorators import login_required
app_name="unidades"

urlpatterns=[
    path('',login_required(indexUnidades),name="indexUnidades"),
    path('agregarUnidad/',login_required(agregarUnidad),name="agregarUnidad"),
    path('eliminar/<int:pk>/', login_required(UnidadDelete.as_view()), name='unidad_eliminar'),

    
]