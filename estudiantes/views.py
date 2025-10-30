from django.shortcuts import render
from django.contrib import messages
from .forms import *
#from django.http import HttpResponse

# Create your views here.

# direcciones de listado query

def estudiante_listado(request):
    query = request.GET.get('q', '').strip()
    mensaje = None
    if query:     #si se busca algo
        query_estudiante = Estudiante.objects.filter(apellido__icontains = query).order_by("nombre")
        #si no se encuentra la busqueda
        if not query_estudiante.exists():
            query_estudiante = Estudiante.objects.all().order_by("apellido")
            mensaje = "No se encontraron estudiantes con ese apellido, mostrando todos los resultados"
    else: 
        # Si no hay búsqueda, no mostrar nada (tabla no aparece)
        # query_estudiante = None
        query_estudiante = Estudiante.objects.all().order_by("apellido")
        
    
    contexto = {"query": query, "query_estudiante": query_estudiante, "mensaje": mensaje}
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
            form = EstudianteForm()  # limpiar el formulario       
    else:
        form = EstudianteForm()    
      
    return render(request, "estudiantes/estudianteregistro.html", {'form': form})
