from django.db import models
from django.core.validators import MaxValueValidator


# Create your models here.


class Domicilio(models.Model):

    calle = models.CharField(max_length=200)
    no_calle = models.IntegerField()
    pais = models.CharField(max_length=50)

    def __str__(self):
        return f'Domicilio {self.id}: {self.calle} {self.no_calle} {self.pais}'

class Persona(models.Model):

    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    edad = models.IntegerField(max_length=99,validators=[MaxValueValidator(99)])

    domicilio = models.ForeignKey(Domicilio,on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'Persona ID: {str(self.id)} - Nombre: {self.nombre} {self.apellido},  {self.email}, edad: {str(self.edad)}'
