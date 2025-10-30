from django.urls import path
from .views import estudiante_listado, estudiante_registro

urlpatterns = [
    path("estlist/", estudiante_listado, name="estudiantelistado"),
    path("estreg/", estudiante_registro, name="estudianteregistro")
]
