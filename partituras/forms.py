from django import forms
from .models import Partitura

class PartituraForm():
    
    class Meta:
        
        model = Partitura
        fields = []