from django.urls import path
from .views import estudiante_listado, estudiante_registro, estudiante_eliminar, estudiante_editar, estudiante_detalle

urlpatterns = [
    path("estlist/", estudiante_listado, name="estudiantelistado"),
    path("estreg/", estudiante_registro, name="estudianteregistro"),
    path("<int:dni>/eliminar", estudiante_eliminar, name="estudianteeliminar"),
    path("<int:dni>/editar", estudiante_editar, name="estudianteeditar"),
    path("<int:dni>/detalle", estudiante_detalle, name="estudiantedetalle"),
]
