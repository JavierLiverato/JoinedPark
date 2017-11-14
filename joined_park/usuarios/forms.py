# -*- coding: 850 -*-
from django import forms
from usuarios.models import *
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import ugettext_lazy as _

class UserForm(UserCreationForm):

    class Meta:
        my_default_errors = {
    'required': 'Este campo es requerido',
    'invalid': 'El valor ingresado no es válido'
    }
        GENERO = (('Masculino', 'Masculino'), ('Femenino', 'Femenino'), ('LGBT', 'LGBT'))
        TIPO_DOCUMENTO = (('Cédula de ciudadanía', 'CC'), ('Tarjeta de identidad', 'TI'), ('Registro civil', 'RC'))
        model = Perfil

        fields = [
            'username', 
            'first_name', 
            'last_name', 
            'rol', 
            'email',
            'genero',
            'numero_documento',
            'tipo_documento','genero',
            'fecha_nacimiento',
            'password1',
            'password2']
        labels = {
            'username': 'Alias (*)',
            'first_name': 'Nombres (*)',
            'last_name': 'Apellidos (*)',
            'rol': 'Rol del usuario (*)',
            'email': 'Correo electrónico',
            'genero': 'Género (*)',
            'numero_documento': 'Número de documento (*)',
            'tipo_documento': 'Tipo de documento (*)',
            'fecha_nacimiento': 'Fecha de nacimiento (*)',
            'password1': 'Contraseña (*)',
            'password2': 'Confirmar contraseña (*)',
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'máximo 30 caracteres'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'rol': forms.Select(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'genero': forms.Select(attrs={'class': 'form-control'}, choices=GENERO),
            'numero_documento': forms.NumberInput(attrs={'class': 'form-control'}),
            'tipo_documento': forms.Select(attrs={'class': 'form-control'}, choices=TIPO_DOCUMENTO),
            'fecha_nacimiento': forms.DateInput(attrs={'class':'datepicker', 'placeholder':'dd/mm/yyyy'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'contraseña'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'confirmar contraseña'}),
        }
        help_texts = {
            'fecha_nacimiento': 'Seleccione una fecha',
        }

class rolForm(forms.ModelForm):

    class Meta:
        model = Rol
        fields = [
            'nombre_rol',
            'descripcion',       ]
        labels = {
            'nombre_rol': 'Nombre del rol (*)',
            'descripcion': 'Descripción del rol (*)',
        }
        widgets = {
            'nombre_rol': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
        }


