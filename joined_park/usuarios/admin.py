from django.contrib import admin
from usuarios.models import Perfil
from usuarios.models import Rol

admin.site.register(Perfil)
admin.site.register(Rol)