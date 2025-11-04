from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import usuariodetalle, usuarioeditar, usuarioregistrar

urlpatterns = [
    path("login/", LoginView.as_view(template_name="cuentas_usuario/usuariologin.html"), name="usuariologin"),
    path("logout/", LogoutView.as_view(template_name='cuentas_usuario/usuariologout.html'), name="usuariologout"), #si no funciona template_name usar next_page al index
    path("detalle/", usuariodetalle, name="usuariodetalle"),
    path("editar/", usuarioeditar, name="usuarioeditar"),
    path("registrar/", usuarioregistrar, name="usuarioregistrar"),
]