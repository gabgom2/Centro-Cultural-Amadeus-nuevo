# core/decorators.py
from functools import wraps
from django.http import HttpResponseForbidden
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from types import FunctionType

def staff_required_login_redirect(view):
    """
    Permite acceso solo a usuarios autenticados y staff.
    Redirige al login si no está autenticado.
    Funciona con FBVs y CBVs.
    """

    def check_user(request, *args, **kwargs):
        LOGIN_URL = reverse("usuariologin")  # se llama aquí, en tiempo de ejecución
        if not request.user.is_authenticated:
            return redirect(f"{LOGIN_URL}?next={request.path}")
        if not request.user.is_staff:
            return HttpResponseForbidden("No tienes permisos para acceder a esta página. Solo staff puede utilizar esta función")
        return view(request, *args, **kwargs)
    
    # FBV
    if isinstance(view, FunctionType):
        return wraps(view)(check_user)
    
    # CBV
    if hasattr(view, 'as_view'):
        view.dispatch = method_decorator(staff_required_login_redirect)(view.dispatch)
        return view
    
    raise TypeError("El decorador solo puede aplicarse a funciones o clases de vistas")
