from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib import messages
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
    pass

class PartituraUpdateView(UpdateView):
    pass

class PartituraDeleteView(DeleteView):
    pass