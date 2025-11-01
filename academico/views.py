from django.shortcuts import render
from .models import Asignatura
from .forms import AsignaturaForm
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib import messages

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