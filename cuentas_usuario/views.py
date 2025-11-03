from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import UsuarioChangeForm, UsuarioCreationForm

# Create your views here.

def registrar(request):
    if request.method == 'POST':
        form = UsuarioCreationForm(request.POST) #request.FILES para cargar archivos
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect("userdetail")
    else:
        form = UsuarioCreationForm()
        
    contexto = {"form": form}
    return render(request, "cuentas/registro.html", contexto)


@login_required
def userdetail(request):
    return render(request, "cuentas/informacion.html", {"usuario": request.user})