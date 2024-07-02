from django.contrib import admin
from .models import *

#class ProfesorAdmin(admin.ModelAdmin):
    #list_display=("apellido","nombre","email","profesion")

class ClienteAdmin(admin.ModelAdmin):
    list_filter=("nombre",)
    list_display=("nombre","apellido","identificacion","email","telefono")

admin.site.register(Cliente,ClienteAdmin)
admin.site.register(Bicicleta)
admin.site.register(Accesorios)
admin.site.register(Rental)

# Register your models here.
