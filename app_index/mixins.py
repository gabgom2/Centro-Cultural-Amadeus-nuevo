from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.shortcuts import redirect

class StaffRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    """Mixin para que solo usuarios con is_staff=True puedan acceder a la vista."""
    login_url = "/cuentas/login/"  # redirige si no está autenticado

    def test_func(self):
        return self.request.user.is_staff
    
    def handle_no_permission(self):
        if not self.request.user.is_authenticated:
            # Usuario no autenticado: usar el comportamiento de LoginRequiredMixin
            return super().handle_no_permission()
        # Usuario autenticado pero no staff: mensaje y redirección
        messages.warning(self.request, "No tienes permisos suficientes para acceder a esta sección.")
        # Redirigir a donde quieras, por ejemplo a la página anterior o a un listado
        next_url = self.request.META.get('HTTP_REFERER', '/')  # intenta volver a la página anterior, si no a '/'
        return redirect(next_url)

    # def handle_no_permission(self):
    #     if not self.request.user.is_authenticated:
    #         return super().handle_no_permission()  # redirige al login
    #     messages.error(self.request, "No tienes permisos para acceder a esta sección.")
    #     return super().handle_no_permission()  # 403 o login según configuración
