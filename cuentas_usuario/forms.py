from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import Usuario

class UsuarioCreationForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ["username", "email"]

class UsuarioChangeForm(UserChangeForm):
    class Meta:
        model = Usuario
        fields = ["username", "descripcion", "ubicacion", "sitio_web", "email", "fecha_de_nacimiento"]
        exclude = ("id",)
        widgets = {
            "descripcion": forms.Textarea(attrs={
                "class": "form-control", 
                "rows": 3,
                "placeholder": "Escribe una breve descripción"
            }),
            "ubicacion": forms.TextInput(attrs={"class": "form-control", "placeholder": "Ciudad, país"}),
            "sitio_web": forms.URLInput(attrs={"class": "form-control", "placeholder": "https://tusitio.com"}),
            "fecha_de_nacimiento": forms.DateInput(attrs={
                "type": "date", 
                "class": "form-control"
            }),
            "avatar": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
        }
        
    # avatar = models.ImageField()
    # descripcion = models.TextField(blank=True),
    # ubicacion = models.CharField(max_length=40, blank=True),
    # sitio_web = models.CharField(max_length=100, blank=True),
    # fecha_de_nacimiento = models.DateField(null=True)
    