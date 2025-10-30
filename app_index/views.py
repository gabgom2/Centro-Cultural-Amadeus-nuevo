from django.shortcuts import render
from datetime import datetime

#from django.contrib import messages
#from django.http import HttpResponse

# Create your views here.

def renderizar_index(request):
    return render(request, "app_index/index.html")

#django.shortcuts -> redirect sirve para redirigir

def about_me(request):
    return render(request, "app_index/about.html")


#***********************************************************
#testing

def testing(request):
    fecha_actual = datetime(2025, 10, 17, 4, 30)
    numeros_unoaldiez = range(1, 11)
    contexto = {"fecha":fecha_actual, "numeros": numeros_unoaldiez}
    return render(request, "app_index/test.html", contexto)

