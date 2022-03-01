from django.urls import path
from apps.material.views import indexMateriales,agregarMaterial, materialEdit,materialEliminar
from .formsets import FormSetMaterial
from django.contrib.auth.decorators import login_required
app_name="materiales"

urlpatterns=[
    path('',login_required(indexMateriales),name="indexMateriales"),
    path('agregarMaterial/',login_required(FormSetMaterial.as_view()),name="agregarMaterial"),
     path('actualizar/<int:id_material>/',login_required(materialEdit), name='materialEdit'),
    path('eliminar/<int:id_material>/',login_required(materialEliminar), name='materialEliminar'), 
    
]