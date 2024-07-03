from django.shortcuts import render
from .models import *
from .forms import *

# Copyright Gabriel Galvan

def home(request):
    return render(request, "AppCoder/index.html")

def clientes(request):
    contexto = {"cliente": Cliente.objects.all()}
    return render(request, "AppCoder/clientes.html", contexto)

def bicicletas(request):
    contexto={"bicicleta": Bicicleta.objects.all()}
    return render(request, "AppCoder/bicicletas.html",contexto)

def accesorios(request):
    contexto={"accesorio":Accesorios.objects.all()}
    return render(request, "AppCoder/accesorios.html",contexto)

def rental(request):
    contexto={"rental":Rental.objects.all()}
    return render(request, "AppCoder/rental.html",contexto)

def acerca(request):
    return render(request, "AppCoder/acerca.html")

def formulario_cliente(request):
    if request.method=='POST':
        clienteForm=ClienteFormulario(request.POST)
        print(clienteForm)
        if clienteForm.is_valid: 
            informacion=clienteForm.cleaned_data
            cliente=Cliente(nombre=informacion['nombre'],apellido=informacion['apellido'],identificacion=informacion['identificacion'],email=informacion['email'],telefono=informacion['telefono'])
            cliente.save()
            contexto={"cliente":Cliente.objects.all()}
            return render(request,"AppCoder/clientes.html")
    else:
        clienteForm=ClienteFormulario()
    return render(request,"AppCoder/cli_Form.html", {"clienteForm": clienteForm})

def formulario_bicicleta(request):
    if request.method=='POST':
        bicicletaForm=BicicletaFormulario(request.POST)
        print(bicicletaForm)
        if bicicletaForm.is_valid: 
            informacion=bicicletaForm.cleaned_data
            bicicleta=Bicicleta(marca=informacion['marca'],modelo=informacion['modelo'],serie=informacion['serie'])
            bicicleta.save()
            contexto={"bicicleta":Bicicleta.objects.all()}
            return render(request,"AppCoder/bicicletas.html")
    else:
        bicicletaForm=BicicletaFormulario()
    return render(request,"AppCoder/bici_Form.html", {"bicicletaForm": bicicletaForm})

def formulario_accys(request):
    if request.method=='POST':
        accyForm=AccesoriosFormulario(request.POST)
        print(accyForm)
        if accyForm.is_valid: 
            informacion=accyForm.cleaned_data
            accesorio=Accesorios(tipo=informacion['tipo'],marca=informacion['marca'])
            accesorio.save()
            contexto={"accesorios":Accesorios.objects.all()}
            return render(request,"AppCoder/accesorios.html")
    else:
        accyForm=AccesoriosFormulario()
    return render(request,"AppCoder/accys_Form.html", {"accyForm": accyForm})

def formulario_rental(request):
    if request.method=='POST':
        rentalForm=RentalFormulario(request.POST)
        print(rentalForm)
        if rentalForm.is_valid: 
            informacion=rentalForm.cleaned_data
            rental=Rental(cant_dias=informacion['cant_dias'],valor=informacion['valor'])
            rental.save()
            contexto={"rental":Rental.objects.all()}
            return render(request,"AppCoder/rental.html")
    else:
        rentalForm=RentalFormulario()
    return render(request,"AppCoder/rent_Form.html", {"rentalForm": rentalForm})

def buscarClientes(request):
    return render(request,"AppCoder/buscar_cliente.html") #ok

def encontrarClientes(request):
    if request.GET['buscar']:
        patron = request.GET['buscar']
        clientes = Cliente.objects.filter(nombre__icontains=patron)
        contexto = {'cliente': clientes}
    else:
        contexto = {'cliente': Cliente.objects.all()}

    return render(request,"AppCoder/clientes.html",contexto)

def buscarBicicletas(request):
    return render(request,"AppCoder/buscar_bicicleta.html") #ok

def encontrarBicicletas(request):
    if request.GET['buscar']:
        patron = request.GET['buscar']
        bicicletas = Bicicleta.objects.filter(marca__icontains=patron)
        contexto = {'bicicleta': bicicletas}
    else:
        contexto = {'bicicleta': Bicicleta.objects.all()}

    return render(request,"AppCoder/bicicletas.html",contexto)

def buscarAccesorios(request):
    return render(request,"AppCoder/buscar_accy.html") #ok

def encontrarAccesorios(request):
    if request.GET['buscar']:
        patron = request.GET['buscar']
        accesorios = Accesorios.objects.filter(tipo__icontains=patron)
        contexto = {'accesorio': accesorios}
    else:
        contexto = {'accesorio': Accesorios.objects.all()}

    return render(request,"AppCoder/accesorios.html",contexto)




    



# Create your views here.
