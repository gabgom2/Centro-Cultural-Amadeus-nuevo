from django.urls import path
from .views import AsignaturaListView, AsignaturaCreateView, AsignaturaDetailView, AsignaturaDeleteView, AsignaturaUpdateView

urlpatterns = [
    path("", AsignaturaListView.as_view(), name="asignaturalistado"),
    path("asigreg/", AsignaturaCreateView.as_view(), name="asignaturaregistro"),
    path("<str:codigo>/detalle", AsignaturaDetailView.as_view(), name="asignaturadetalle"),
    path("<str:codigo>/editar", AsignaturaUpdateView.as_view(), name="asignaturaeditar"),
    path("<str:codigo>/eliminar", AsignaturaDeleteView.as_view(), name="asignaturaeliminar"),
]
