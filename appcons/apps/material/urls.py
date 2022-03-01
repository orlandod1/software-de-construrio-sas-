from django.urls import path
from apps.material.views import indexMateriales, materialDelete, materialEdit
from .formsets import FormSetMaterial
from django.contrib.auth.decorators import login_required
app_name="materiales"

urlpatterns=[
    path('',login_required(indexMateriales),name="indexMateriales"),
    path('agregarMaterial/',login_required(FormSetMaterial.as_view()),name="agregarMaterial"),
     path('actualizar/<int:id_material>/',login_required(materialEdit), name='materialEdit'),
    path('eliminar-material/<int:id>/',login_required(materialDelete), name='material_delete'), 
    
]