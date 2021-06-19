from django.db import models

# Create your models here.


class Registro(models.Model):
    correo = models.CharField(
        max_length=100, verbose_name='Correo Electronico')
    usuario = models.CharField(
        max_length=10, primary_key=True, verbose_name='Usuario')
    contraseña = models.CharField(max_length=20, verbose_name='Contraseña')
    fchnac = models.DateField(verbose_name='Fecha de Nacimiento')

    def __str__(self):
        return (self.usuario)
