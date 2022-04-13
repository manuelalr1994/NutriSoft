from django.db import models

class Pacientes(models.Model):
    codigo = models.CharField(max_length=5)
    nombre = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    sexo = models.CharField(max_length=10)
    fecha_nacimiento = models.DateField()
    escolaridad = models.CharField(max_length=10)
    tipo_sangre = models.CharField(max_length=3)
    estado_civil = models.CharField(max_length=10)
    activo = models.BooleanField(default=True)