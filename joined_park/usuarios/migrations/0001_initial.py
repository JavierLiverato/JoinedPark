# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django.contrib.auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('numero_documento', models.BigIntegerField()),
                ('tipo_documento', models.CharField(max_length=50)),
                ('genero', models.CharField(max_length=20)),
                ('fecha_nacimiento', models.CharField(max_length=20)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre_rol', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name_plural': 'Roles',
            },
        ),
        migrations.AddField(
            model_name='perfil',
            name='rol',
            field=models.ForeignKey(to='usuarios.Rol'),
        ),
    ]
