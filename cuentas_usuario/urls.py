from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import usuariodetalle, usuarioeditar, usuarioregistrar

urlpatterns = [
    path("login/", LoginView.as_view(template_name="cuentas_usuario/login.html"), name="usuariologin"),
    path("logout/", LogoutView.as_view(template_name="cuentas_usuario/logout.html"), name="usuariologout"),
    path("detalle/", usuariodetalle, name="usuariodetalle"),
    path("editar/", usuarioeditar, name="usuarioeditar"),
    path("registrar/", usuarioregistrar, name="usuarioregistrar"),
]