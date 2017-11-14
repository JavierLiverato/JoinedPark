from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.

class Perfil(User):
    rol = models.ForeignKey('Rol')
    numero_documento = models.BigIntegerField()
    tipo_documento = models.CharField(max_length=50)
    genero = models.CharField(max_length=20)
    fecha_nacimiento = models.CharField(max_length=20)


class Rol(models.Model):
    nombre_rol = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=250)

    class Meta: 
        verbose_name_plural = 'Roles'

    def __unicode__(self): 
        return '%s' % (self.nombre_rol)