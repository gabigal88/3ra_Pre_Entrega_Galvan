# 3ra_Pre_Entrega_Galvan

# La pagina es para un Bike Rental y contiene las tarifas diarias, bicicletas y accesorios (guantes, cascos,etc)
# Permite registrar clientes en la base de datos para las reservas que se realizan, aunque cabe destacar que en un principio solo almacena datos

# los modelos creados son Cliente,Bicicleta,Accesorios,Rental. Mas adelante la idea es agregar una clase Circuitos y Guias para que no solo se puedan resevrar bicicletas sino tambien poder realizar circuitos con profesores/guias

#Se crearon los formularios correspondientes para realizar carga de datos y las busquedas para Clientes, Bicicletas y Accesorios. los path de busqueda a continuacion:

    path('buscarClientes/', buscarClientes,name="buscarClientes"),
    path('encontrarClientes/', encontrarClientes,name="encontrarClientes"),
    path('buscarBicicletas/', buscarBicicletas,name="buscarBicicletas"),
    path('encontrarBicicletas/', encontrarBicicletas,name="encontrarBicicletas"),
    path('buscarAccesorios/', buscarAccesorios,name="buscarAccesorios"),
    path('encontrarAccesorios/', encontrarAccesorios,name="encontrarAccesorios"),
