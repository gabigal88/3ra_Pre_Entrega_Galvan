from django.db import models

class Cliente(models.Model):
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    identificacion=models.IntegerField()
    email=models.EmailField()
    telefono=models.IntegerField()

    class Meta:
        ordering=["identificacion"]
    
    def __str__(self):
        return f'{self.nombre}'

class Bicicleta(models.Model):
    marca=models.CharField(max_length=20)
    modelo=models.CharField(max_length=20)
    serie=models.CharField(max_length=20)
    suspension=models.CharField(max_length=20)
    def __str__(self):
        return f'{self.marca},{self.modelo},{self.serie},{self.suspension}'

class Accesorios(models.Model):
    tipo=models.CharField(max_length=20)
    marca=models.CharField(max_length=20)
    def __str__(self):
        return f'{self.tipo},{self.marca}'

    class Meta:
        verbose_name="Accesorios"
        verbose_name_plural="Accesorios"
        ordering=["tipo","marca"]

class Rental(models.Model):
    cant_dias=models.IntegerField()
    valor=models.IntegerField()   #valor diario
    #pago=models.BooleanField()
