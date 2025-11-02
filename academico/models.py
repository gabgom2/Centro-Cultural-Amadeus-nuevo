from django.db import models
import uuid

class Asignatura(models.Model):

    nivel = [
        ("Inicial", "inicial"),
        ("Intermedio", "intermedio"),
        ("Avanzado", "avanzado"),
    ]
    
    nombre = models.CharField(max_length=100, unique=True)
    nivel = models.CharField(max_length = 16, choices=nivel, default=nivel[0])
    horas_catedra = models.IntegerField(default=20)
    
    #autoasignadas
     
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
        return str(self.codigo)[-12:]
  
    def __str__(self):
        return f"Asignatura: {self.nombre} / Nivel: {self.nivel} / Código: {self.codigo}"
    
# **************************************************************************
# Viejas funciones de generación de código (pk) a modo de referencia
#
# import uuid
#
# def generar_codigo():
#     return uuid.uuid4().hex
#
# class Asignatura(models.Model):
    
#     nombre = models.CharField(max_length=30)
#     codigo = models.IntegerField(unique=True, blank=True, null=True)

#     def generar_codigo(self):
#         #Aumentar el código actual
#         codigo_anterior = Asignatura.objects.all().order_by('codigo').last()
        
#         if codigo_anterior:
#             return codigo_anterior.codigo + 1
#         else:
#             return 100 #valor inicial
        
#     def save(self, *args, **kwargs):
#     # Si el codigo no está asignado se generará antes de guardarse
#         if self.codigo is None:
#             self.codigo = self.generar_codigo()
#         super(Asignatura, self).save(*args, **kwargs)

# Otra opción es auto-incrementar id con = models.Autofield()
# **************************************************************************