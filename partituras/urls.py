from django.urls import path
from .views import PartituraCreateView, PartituraDeleteView, PartituraDetailView, PartituraListView, PartituraUpdateView


urlpatterns = [path("", PartituraListView.as_view(), name="partituralistado"),
        path("partreg/", PartituraCreateView.as_view(), name="partituraregistro"),
        path("<str:codigo>/detalle", PartituraDetailView.as_view(), name="partituradetalle"),
        path("<str:codigo>/ver_pdf/", PartituraDetailView.ver_pdf_view, name="ver_pdf"),
        path("<str:codigo>/editar", PartituraUpdateView.as_view(), name="partituraeditar"),
        path("<str:codigo>/eliminar", PartituraDeleteView.as_view(), name="partituraeliminar"),
 ]
