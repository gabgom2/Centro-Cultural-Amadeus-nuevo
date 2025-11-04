from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import UsuarioChangeForm, UsuarioCreationForm
from django.contrib import messages

# Create your views here.

def usuarioregistrar(request):
    if request.method == 'POST':
        form = UsuarioCreationForm(request.POST) #request.FILE para cargar archivos
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect("usuariodetalle")
    else:
        form = UsuarioCreationForm()
        
    contexto = {"form": form}
    return render(request, "cuentas_usuario/usuarioregistro.html", contexto)


@login_required
def usuariodetalle(request):
    return render(request, "cuentas_usuario/usuariodetalle.html", {"usuario": request.user})


@login_required
def usuarioeditar(request):
    user = request.user
    if request.method == "POST":
        form = UsuarioChangeForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "Perfil actualizado correctamente.")
            return redirect("usuariodetalle")
    else:
        form = UsuarioChangeForm(instance=user)

    return render(request, "cuentas_usuario/usuarioeditar.html", {"form": form, "usuario": user})