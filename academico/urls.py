from django.urls import path
from .views import AsignaturaListView, AsignaturaCreateView, AsignaturaDetailView, AsignaturaDeleteView, AsignaturaUpdateView

urlpatterns = [
    path("", AsignaturaListView.as_view(), name="asignaturalistado"),
    path("asigreg/", AsignaturaCreateView.as_view(), name="asignaturaregistro"),
    path("<str:codigo>/detalle", AsignaturaDetailView.as_view(), name="asignaturadetalle"),
    #path("<int:dni>/editar", estudiante_editar, name="estudianteeditar"),
    #path("<int:dni>/detalle", estudiante_detalle, name="estudiantedetalle"),
]
