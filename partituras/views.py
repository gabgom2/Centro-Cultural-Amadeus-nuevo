from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib import messages
#from .models import
#from .forms import

# Create your views here.

class PartituraListView(ListView):
    pass

class PartituraCreateView(CreateView):
    pass

class PartituraDetailView(DetailView):
    pass

class PartituraUpdateView(UpdateView):
    pass

class PartituraDeleteView(DeleteView):
    pass