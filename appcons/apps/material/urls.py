from django.urls import path
from apps.material.views import indexMateriales,agregarMaterial
from .formsets import FormSetMaterial
app_name="materiales"

urlpatterns=[
    path('',indexMateriales,name="indexMateriales"),
    path('agregarMaterial/',FormSetMaterial.as_view(),name="agregarMaterial"),
    
]