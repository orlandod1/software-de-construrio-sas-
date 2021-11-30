from django.urls import path
from apps.material.views import indexMateriales,agregarMaterial
app_name="materiales"

urlpatterns=[
    path('',indexMateriales,name="indexMateriales"),
    path('agregarMaterial/',agregarMaterial,name="agregarMaterial")
]