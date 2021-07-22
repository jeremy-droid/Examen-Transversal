from django.db import models
# Create your models here.




#Clase Pais.
class Pais(models.Model):
    pais = models.IntegerField(primary_key=True, verbose_name="Id de Pais")
    nombrePais = models.CharField(max_length=50, verbose_name="Nombre del Pais")

    def __str__(self):
        return self.nombrePais





#Clase Moneda.
#class Moneda(models.Model):
#    moneda = models.IntegerField(primary_key=True, verbose_name="Id Moneda")
#    tipoMoneda = models.CharField(max_length=50, verbose_name="Tipo de moneda")
#    def __str__(self):
#        return self.tipoMoneda

# Clase Proveedor.
class Proveedor(models.Model):

    identificacion = models.CharField(max_length=6, primary_key=True, verbose_name="Numero de Identificacion")

    nombre = models.CharField(max_length=50, verbose_name="Nombre")

    telefono = models.CharField ( max_length=12, verbose_name="Telefono" ) 

    direccion = models.CharField(max_length=100, verbose_name="Direccion")

    email = models.CharField(max_length=50, verbose_name="Email")

    contraseña = models.CharField(max_length=50, verbose_name="Contraseña")

    pais = models.CharField(max_length=50, verbose_name="Pais")
    
    moneda =  models.ForeignKey(Pais, on_delete=models.CASCADE)

    def __str__(self):
        return self.identificacion