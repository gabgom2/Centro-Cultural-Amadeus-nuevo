from django import forms
from .models import Estudiante

class EstudianteForm(forms.ModelForm):
    class Meta:
        
        model = Estudiante
        fields = ["apellido", "nombre", "dni", "telefono", "barrio_residencia", "email"]