from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import Usuario

class UsuarioCreationForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ["username", "email"]

# class UsuarioChangeForm(UserChangeForm):
#     class Meta:
#         model = Usuario
#         fields = ["username", "descripcion", "ubicacion", "sitio_web", "email", "fecha_de_nacimiento", "avatar"]
#         exclude = ("id",)
#         widgets = {
#             "descripcion": forms.Textarea(attrs={
#                 "class": "form-control", 
#                 "rows": 3,
#                 "placeholder": "Escribe una breve descripción"
#             }),
#             "ubicacion": forms.TextInput(attrs={"class": "form-control", "placeholder": "Ciudad, país"}),
#             "sitio_web": forms.URLInput(attrs={"class": "form-control", "placeholder": "https://tusitio.com"}),
#             "fecha_de_nacimiento": forms.DateInput(attrs={
#                 "type": "date", 
#                 "class": "form-control"
#             }),
#             "avatar": forms.ClearableFileInput(attrs={"class": "form-control"}),
#             "username": forms.TextInput(attrs={"class": "form-control"}),
#             "email": forms.EmailInput(attrs={"class": "form-control"}),
#         }
    
class UsuarioChangeForm(forms.ModelForm):
    password1 = forms.CharField(
        label="Nueva contraseña",
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
        required=False,
        help_text="Dejar vacío si no quieres cambiarla."
    )
    password2 = forms.CharField(
        label="Confirmar nueva contraseña",
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
        required=False
    )

    class Meta:
        model = Usuario
        fields = ["username", "descripcion", "ubicacion", "sitio_web", "email", "fecha_de_nacimiento", "avatar"]
        widgets = {
            "descripcion": forms.Textarea(attrs={"class": "form-control", "rows": 3, "placeholder": "Escribe una breve descripción"}),
            "ubicacion": forms.TextInput(attrs={"class": "form-control", "placeholder": "Ciudad, país"}),
            "sitio_web": forms.URLInput(attrs={"class": "form-control", "placeholder": "https://tusitio.com"}),
            "fecha_de_nacimiento": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            "avatar": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
        }

    def clean(self):
        cleaned_data = super().clean()
        pwd1 = cleaned_data.get("password1")
        pwd2 = cleaned_data.get("password2")

        if pwd1 or pwd2:  # Si el usuario intenta cambiar la contraseña
            if pwd1 != pwd2:
                raise forms.ValidationError("Las contraseñas no coinciden.")
            if len(pwd1) < 8:
                raise forms.ValidationError("La contraseña debe tener al menos 8 caracteres.")

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        pwd1 = self.cleaned_data.get("password1")
        if pwd1:
            user.set_password(pwd1)  # Actualiza la contraseña
        if commit:
            user.save()
        return user
    