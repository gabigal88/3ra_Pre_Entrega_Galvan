from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class ClienteFormulario(forms.Form):

    nombre=forms.CharField(max_length=50,required=True,label="Nombre de Cliente")
    apellido=forms.CharField(max_length=50,required=True,label="Apellido de Cliente")
    identificacion=forms.IntegerField(required=True)
    email=forms.EmailField(required=True)
    telefono=forms.IntegerField(required=True)

class BicicletaFormulario(forms.Form):

    marca=forms.CharField()
    modelo=forms.CharField()
    serie=forms.CharField()
    suspension=forms.CharField()
    disponibilidad=forms.CheckboxInput()

class AccesoriosFormulario(forms.Form):

    tipo=forms.CharField()
    marca=forms.CharField()

class RentalFormulario(forms.Form):

    cant_dias=forms.CharField()
    valor=forms.IntegerField()

class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Contraseña a confirmar", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
