from django.urls import path
from .views import estudiante_listado

urlpatterns = [
    path("estlist/", estudiante_listado, name="estudiantelistado")
    
]
