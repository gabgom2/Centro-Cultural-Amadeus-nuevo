from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import *
#from django.http import HttpResponse

# Create your views here.

# direcciones de listado query

def estudiante_listado(request):
    query = request.GET.get('q', '').strip()
    
    if query:     #si se busca algo
        query_estudiante = Estudiante.objects.filter(apellido__icontains = query).order_by("nombre")
        #si no se encuentra la busqueda
        if not query_estudiante.exists():
            query_estudiante = Estudiante.objects.all().order_by("apellido")
            messages.warning(request, "No se encontraron estudiantes con ese apellido, mostrando todos los resultados.")
    else: 
        query_estudiante = Estudiante.objects.all().order_by("apellido")
            
    contexto = {"query": query, "query_estudiante": query_estudiante}
    return render(request, "estudiantes/estudiantelistado.html", contexto)

#FORM estudiantes

def estudiante_registro(request):

    # GET - Pedir info a la base de datos
    # POST - Solicitud para crear info / manipular datos
    
    if request.method == "POST":
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Estudiante registrado/a con éxito.")
            return redirect("estudiantelistado")
            #form = EstudianteForm()  # limpiar el formulario
    else:
        form = EstudianteForm()    
      
    return render(request, "estudiantes/estudianteregistro.html", {'form': form})

def estudiante_eliminar(request, dni):
    estudiante = get_object_or_404(Estudiante, dni=dni)
    estudiante.delete()
    messages.success(request, "Estudiante eliminado con éxito")
    return redirect("estudiantelistado")

def estudiante_editar(request, dni):
    estudiante = get_object_or_404(Estudiante, dni=dni)
    if request.method == "POST":
        form = EstudianteForm(request.POST, instance=estudiante)
        if form.is_valid():
            form.save()
            messages.success(request, "Estudiante modificado con éxito.")
            #form = EstudianteForm()  # limpiar el formulario       
            return redirect("estudiantelistado")
    else:        # IF request.method == GET / debería instanciar un formulario si lo voy a enviar por contexto
        form = EstudianteForm(instance=estudiante)   
    
    contexto = {"form":form, "edicion":True}
    return render(request, "estudiantes/estudianteregistro.html", contexto)

def estudiante_detalle(request, dni):
    estudiante = get_object_or_404(Estudiante, dni=dni)
    return render(request, "estudiantes/estudiantedetalle.html", {"estudiante": estudiante})
        