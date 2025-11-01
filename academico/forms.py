from django import forms
from .models import Asignatura

class AsignaturaForm(forms.ModelForm):
    
    class Meta:
        
        model = Asignatura
        fields = ["nombre", "nivel", "horas_catedra"]
#**************************************************************************
# Vieja función de generación de attr 'form-control' para cada widget a modo de referencia
# def agregar_form_control():
#     def __init__(self, *args, **kwargs):
#             super().__init__(*args, **kwargs)
#             for field in self.fields.values():
#                 field.widget.attrs.update({
#                     'class': 'form-control'
#                 })
#**************************************************************************