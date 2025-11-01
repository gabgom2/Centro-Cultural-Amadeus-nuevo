from django.urls import path
from .views import AsignaturaListView

urlpatterns = [
    path("", AsignaturaListView.as_view(), name="asignaturalistado"),
    #path("estreg/", estudiante_registro, name="estudianteregistro"),
    #path("<int:dni>/eliminar", estudiante_eliminar, name="estudianteeliminar"),
    #path("<int:dni>/editar", estudiante_editar, name="estudianteeditar"),
    #path("<int:dni>/detalle", estudiante_detalle, name="estudiantedetalle"),
]
