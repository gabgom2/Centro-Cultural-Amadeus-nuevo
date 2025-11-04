from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib import messages
from django.http import FileResponse, Http404
from .models import Partitura
from .forms import PartituraForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.


class PartituraListView(LoginRequiredMixin, ListView): # LoginReq Mix: Solo usuarios registrados! 
    model = Partitura
    template_name = "partituras/partituralistado.html"
    context_object_name = "partituras"


class PartituraCreateView(LoginRequiredMixin, CreateView):
    model = Partitura
    form_class = PartituraForm
    template_name = "partituras/partituraregistro.html"
    success_url = reverse_lazy("partituralistado")
    
    
    def form_valid(self, form):
        messages.success(self.request, f"La partitura '{form.instance.titulo}' fue subida correctamente.")
        return super().form_valid(form)

class PartituraDetailView(LoginRequiredMixin, DetailView):
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

class PartituraUpdateView(LoginRequiredMixin, UpdateView):
    model = Partitura
    form_class = PartituraForm
    template_name = "partituras/partituraregistro.html"  # plantilla para crear/editar
    success_url = reverse_lazy("partituralistado")
    slug_field = "codigo"
    slug_url_kwarg = "codigo"

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f"La partitura '{self.object.titulo}' fue modificada correctamente.")
        return response
    
class PartituraDeleteView(LoginRequiredMixin, DeleteView):
    model = Partitura
    template_name = "partituras/partituraeliminar.html"  # plantilla de confirmación
    slug_field = "codigo"
    slug_url_kwarg = "codigo"
    success_url = reverse_lazy("partituralistado")

    def post(self, request, *args, **kwargs):
        # Sobrescribimos post() para mostrar mensaje antes de redirigir
        obj = self.get_object()
        obj_name = obj.titulo
        obj.delete()
        messages.success(request, f"La partitura '{obj_name}' fue eliminada correctamente.")
        return redirect(self.success_url)
