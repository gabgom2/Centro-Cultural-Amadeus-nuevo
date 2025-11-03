from django.db import models
import uuid

# Create your models here.

class Partitura(models.Model):
    
    titulo = models.CharField(max_length=100, unique=True)
    autor = models.CharField(max_length=80)
    arreglista = models.CharField(blank=True,max_length=80)
    archivo = models.FileField(upload_to='scoresheets/')
    
    #auto generados
    codigo = models.UUIDField(
                    primary_key=True,  #No poner null=True o blank=True en pk, error
                    default=uuid.uuid4,
                    unique=True,
                    editable=False,
                )
    
    fecha_registro = models.DateTimeField(auto_now_add=True) #Fecha de registro se asigna en el momento de creación por auto_now_add
    
    # Guardar solo los últimos 12 caracteres del código para mostrar en la tabla
    @property
    def codigo_corto(self):
        ultimos = int(self.codigo.int % 10**12)
        # Devuelve como string de 12 dígitos, rellenando con ceros a la izquierda si es necesario
        return f"{ultimos:012d}"
    
    def __str__(self):
        return f"Partitura: {self.titulo} / Autor: {self.autor} / Código: {self.codigo_corto}"
    
    
    
    #titulo
    #autor
    #arreglista
    #isbn
    #codigo