from django.urls import path
from AppCoder.views import *
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('', home,name="home"),
    path('clientes',clientes,name="clientes"),
    path('bicicletas', bicicletas, name="bicicletas"),
    path('accesorios', accesorios, name="accesorios"),
    path('rental', rental,name="rental"),
    path('acerca', acerca,name="acerca"),
    path('cli_Form', formulario_cliente,name="cli_Form"),
    path('bici_Form', formulario_bicicleta,name="bici_Form"),
    path('accys_Form', formulario_accys,name="accys_Form"),
    path('rent_Form', formulario_rental,name="rent_Form"),
    path('buscarClientes/', buscarClientes,name="buscarClientes"),
    path('encontrarClientes/', encontrarClientes,name="encontrarClientes"),
    path('buscarBicicletas/', buscarBicicletas,name="buscarBicicletas"),
    path('encontrarBicicletas/', encontrarBicicletas,name="encontrarBicicletas"),
    path('buscarAccesorios/', buscarAccesorios,name="buscarAccesorios"),
    path('encontrarAccesorios/', encontrarAccesorios,name="encontrarAccesorios"),
]