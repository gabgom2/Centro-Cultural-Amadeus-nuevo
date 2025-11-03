from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

def avatar_upload_to(instance, filename):
    return f"avatars/{instance.username}/{filename}"

class Usuario(AbstractUser):
    avatar = models.ImageField(
        upload_to=avatar_upload_to,
        default="default/avatar_black.jpg",
        blank=True,
        
        
    )
    descripcion = models.TextField(blank=True),
    ubicacion = models.CharField(max_length=40, blank=True),
    sitio_web = models.CharField(max_length=100, blank=True),
    fecha_de_nacimiento = models.DateField(null=True)
    
    def __str__(self):
        return f"Usuario: {self.username} / Mail: {self.email} / Es staff: {self.is_staff} / Es superuser: {self.is_superuser}"


    