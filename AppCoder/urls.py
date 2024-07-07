from django.urls import path
from AppCoder.views import *
#from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', home,name="home"),

    #__clientes
    path('clientes',clientes,name="clientes"),
    path('cli_Form', formulario_cliente,name="cli_Form"),
    path('clienteUpdate/<id_cliente>/', clienteUpdate, name="clienteUpdate"),
    path('clienteDelete/<id_cliente>/', clienteDelete, name="clienteDelete"),
    path('buscarClientes/', buscarClientes,name="buscarClientes"),
    path('encontrarClientes/', encontrarClientes,name="encontrarClientes"),

    #__bicicletas
    path('bicicletas', BicicletaList.as_view(), name="bicicletas"),
    #path('bici_Form', formulario_bicicleta,name="bici_Form"),
    path('bicicletaCreate/', BicicletaCreate.as_view(), name="bicicletaCreate"), 
    path('bicicletaUpdate/<int:pk>/', BicicletaUpdate.as_view(), name="bicicletaUpdate"), 
    path('bicicletaDelete/<int:pk>/', BicicletaDelete.as_view(), name="bicicletaDelete"),

    path('accesorios', accesorios, name="accesorios"),
    path('rental', rental,name="rental"),
    path('acerca', acerca,name="acerca"),


    path('accys_Form', formulario_accys,name="accys_Form"),
    path('rent_Form', formulario_rental,name="rent_Form"),

    path('buscarBicicletas/', buscarBicicletas,name="buscarBicicletas"),
    path('encontrarBicicletas/', encontrarBicicletas,name="encontrarBicicletas"),
    path('buscarAccesorios/', buscarAccesorios,name="buscarAccesorios"),
    path('encontrarAccesorios/', encontrarAccesorios,name="encontrarAccesorios"),

    #___ Login / Logout / Registration
    path('login/', loginRequest, name="login"),
    path('logout/', LogoutView.as_view(template_name="AppCoder/logout.html"), name="logout"),
    path('registro/', register, name="registro"),
]