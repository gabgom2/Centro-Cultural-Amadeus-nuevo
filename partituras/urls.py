from django.urls import path
from .views import PartituraCreateView, PartituraDeleteView, PartituraDetailView, PartituraListView, PartituraUpdateView


urlpatterns = [path("", PartituraListView.as_view(), name="partituralistado"),
        path("partreg/", PartituraCreateView.as_view(), name="partituraregistro"),
#        path("<str:codigo>/detalle", PartituraDetailView.as_view(), name=""),
#        path("<str:codigo>/editar", PartituraUpdateView.as_view(), name=""),
#        path("<str:codigo>/eliminar", PartituraDeleteView.as_view(), name=""),
 ]
