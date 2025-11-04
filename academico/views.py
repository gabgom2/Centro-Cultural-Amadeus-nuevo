from django.shortcuts import render, redirect
from .models import Asignatura
from .forms import AsignaturaForm
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from app_index.mixins import StaffRequiredMixin

# Create your views here.

class AsignaturaListView(ListView):
    model = Asignatura
    template_name = "academico/asignaturalistado.html"
    context_object_name = "asignaturas"
    
    def get_queryset(self):
        
        query = self.request.GET.get('q', '').strip()
        
        if query:     #si se busca algo
            query_asignatura = Asignatura.objects.filter(nombre__icontains = query).order_by("nivel")
            #si no se encuentra la busqueda
            if not query_asignatura.exists():
                query_asignatura = Asignatura.objects.all().order_by("nivel")
                messages.warning(self.request, "No se encontró dicha asignatura, mostrando todos los resultados.")
        else: 
            query_asignatura = Asignatura.objects.all().order_by("nombre")
            
        return query_asignatura
    
class AsignaturaCreateView(StaffRequiredMixin, CreateView):
    model = Asignatura
    form_class = AsignaturaForm
    template_name = "academico/asignaturaregistro.html"
    success_url = reverse_lazy("asignaturalistado")
    
    def form_valid(self, form):
        # se guarda el objeto en response
        response = super().form_valid(form)
        messages.success(self.request, f"La asignatura '{self.object.nombre}' fue creada correctamente")

        return response

class AsignaturaDetailView(LoginRequiredMixin, DetailView):
    model = Asignatura
    template_name = "academico/asignaturadetalle.html"
    context_object_name = "asignatura"
    slug_field = "codigo"
    slug_url_kwarg = "codigo"

class AsignaturaUpdateView(StaffRequiredMixin, UpdateView):
    model = Asignatura
    form_class = AsignaturaForm
    template_name = "academico/asignaturaregistro.html"
    success_url = reverse_lazy("asignaturalistado")
    slug_field = "codigo"
    slug_url_kwarg = "codigo"
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f"La asignatura '{self.object.nombre}' fue modificada correctamente.")
        return response

    
class AsignaturaDeleteView(StaffRequiredMixin, DeleteView):
    model = Asignatura
    template_name = "academico/asignaturaeliminar.html"
    slug_field = "codigo"
    slug_url_kwarg = "codigo"
    success_url = reverse_lazy("asignaturalistado")
    
    
    def post(self, request, *args, **kwargs):
        #Se sobreescribe post() en lugar de delete() para asegurar ejecución del mensaje
        obj = self.get_object()
        obj_name = obj.nombre
        obj.delete()
        messages.success(request, f"La asignatura '{obj_name}' fue eliminada correctamente.")
        return redirect(self.success_url)
    
