from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib import messages
from django.http import FileResponse, Http404
from .models import Partitura
from .forms import PartituraForm


# Create your views here.

class PartituraListView(ListView):
    model = Partitura
    template_name = "partituras/partituralistado.html"
    context_object_name = "partituras"

class PartituraCreateView(CreateView):
    model = Partitura
    form_class = PartituraForm
    template_name = "partituras/partituraregistro.html"
    success_url = reverse_lazy("partituralistado")
    
    
    def form_valid(self, form):
        messages.success(self.request, f"La partitura '{form.instance.titulo}' fue subida correctamente.")
        return super().form_valid(form)

class PartituraDetailView(DetailView):
    model = Partitura
    template_name = "partituras/partituradetalle.html"
    context_object_name = "partitura"
    slug_field = "codigo"
    slug_url_kwarg = "codigo"
    
    def ver_pdf(self, request):
        partitura = self.get_object()
        if not partitura.archivo:
            raise Http404("Archivo no encontrado")

        response = FileResponse(open(partitura.archivo.path, 'rb'), content_type='application/pdf')
        response["X-Frame-Options"] = "SAMEORIGIN"
        return response

    @classmethod
    def ver_pdf_view(cls, request, codigo):
        """Método auxiliar para exponer ver_pdf como vista"""
        self = cls()
        self.kwargs = {'codigo': codigo}
        return self.ver_pdf(request)

class PartituraUpdateView(UpdateView):
    pass

class PartituraDeleteView(DeleteView):
    pass