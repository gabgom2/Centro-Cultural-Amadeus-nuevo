from django.urls import path
from .views import estudiante_listado, estudiante_registro, estudiante_eliminar

urlpatterns = [
    path("estlist/", estudiante_listado, name="estudiantelistado"),
    path("estreg/", estudiante_registro, name="estudianteregistro"),
    path("<int:dni>/eliminar", estudiante_eliminar, name="estudianteeliminar")
]
