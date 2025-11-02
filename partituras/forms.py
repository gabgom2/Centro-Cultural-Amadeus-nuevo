from django import forms
from .models import Partitura

class PartituraForm(forms.ModelForm):
    
    class Meta:
        
        model = Partitura
        fields = ["titulo", "autor", "arreglista", "archivo"]
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'autor': forms.TextInput(attrs={'class': 'form-control'}),
            'arreglista': forms.TextInput(attrs={
                'placeholder': 'Campo opcional, dejar blanco si coincide con el autor',
                'class': 'form-control',  # 👈 Esto aplica el estilo
                #'rows': 3,  
            }),
            'archivo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }