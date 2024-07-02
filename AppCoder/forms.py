from django import forms

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
