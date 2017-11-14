# -*- coding: 850 -*-

from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from usuarios.forms import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def nuevo_usuario(request):
    informacion = "inicializando"
    titulo="Nuevo usuario"
    if request.method == 'GET':
        form = UserForm()
        return render_to_response('add.html', 
            locals(), 
            context_instance=RequestContext(request)
        )
    else:#POST
        form = UserForm(request.POST) 
        info = "inicializando"
        if form.is_valid():
            form.save()
            informacion = "Guardado"
        else:
            informacion = "Error"
        return render_to_response(
            'add.html', 
            locals(),
            context_instance=RequestContext(request)
        )
    return render_to_response('add.html', 
        locals(),
        context_instance=RequestContext(request)
    )


def actualizar_usuario(request, id):
    usuario = User.objects.get(id=id)
    informacion = "Procesando"
    titulo="Actualizar datos del usuario"
    if request.method == 'GET':
        form = UserForm(instance=usuario)
    else:
        form = UserForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            informacion = "Guardado"
            return render_to_response(
                'add.html', 
                locals(),
                context_instance=RequestContext(request)
            )
        else:
            informacion = "Error"
            return render_to_response(
                'add.html', 
                locals(),
                context_instance=RequestContext(request)
            )
    return render_to_response('add.html', 
        locals(),
        context_instance=RequestContext(request)
    )


def lista_usuarios(request):
    titulo = "Usuarios registrados"
    usuarios = User.objects.all()
    paginator = Paginator(usuarios, 10)

    page = request.GET.get('page')
    try:
        registros = paginator.page(page)
    except PageNotAnInteger:
        registros = paginator.page(1)
    except EmptyPage:
        registros = paginator.page(paginator.num_pages)
    return render_to_response(
        'lista_usuarios.html', 
        locals(), 
        context_instance=RequestContext(request)
    )


def eliminar_usuario(request, id):
    usuario = Perfil.objects.get(id=id)
    informacion = 'Procesando'
    if request.method == 'GET':
        try:
            usuario.delete()
            informacion = 'Eliminado'
        except Exception, e:
            print e
            informacion = 'No eliminado'
            return render_to_response(
                'lista_usuarios.html', 
                locals(), 
                context_instance=RequestContext(request)
            )
    
    return redirect("usuarios:lista_usuarios")


def nuevo_rol(request):
    informacion = "inicializando"
    titulo="Nuevo rol"
    if request.method == 'GET':
        form = rolForm()
        return render_to_response('add.html', 
            locals(), 
            context_instance=RequestContext(request)
        )
    else:
        form = rolForm(request.POST) 
        info = "inicializando"
        if form.is_valid():
            form.save()
            informacion = "Guardado"
        else:
            informacion = "Error"
        return render_to_response(
            'add.html', 
            locals(),
            context_instance=RequestContext(request)
        )
    return render_to_response('add.html', 
        locals(),
        context_instance=RequestContext(request)
    )


def actualizar_rol(request, id):
    rol = Rol.objects.get(id=id)
    informacion = "Procesando"
    titulo="Actualizar datos del rol de usuario"
    if request.method == 'GET':
        form = rolForm(instance=rol)
    else:
        form = rolForm(request.POST, instance=rol)
        if form.is_valid():
            form.save()
            informacion = "Guardado"
            return render_to_response(
                'add.html', 
                locals(),
                context_instance=RequestContext(request)
            )
        else:
            informacion = "Error"
            return render_to_response(
                'add.html', 
                locals(),
                context_instance=RequestContext(request)
            )
    return render_to_response('add.html', 
        locals(),
        context_instance=RequestContext(request)
    )


def lista_roles(request):
    titulo = "Roles de usuario registrados"
    roles = Rol.objects.all()
    paginator = Paginator(roles, 10)

    page = request.GET.get('page')
    try:
        registros = paginator.page(page)
    except PageNotAnInteger:
        registros = paginator.page(1)
    except EmptyPage:
        registros = paginator.page(paginator.num_pages)
    return render_to_response(
        'lista_roles.html', 
        locals(), 
        context_instance=RequestContext(request)
    )


def eliminar_rol(request, id):
    rol = Rol.objects.get(id=id)
    informacion = 'Procesando'
    if request.method == 'GET':
        try:
            rol.delete()
            informacion = 'Eliminado'
        except Exception, e:
            print e
            informacion = 'No eliminado'
            return render_to_response(
                'lista_roles.html', 
                locals(), 
                context_instance=RequestContext(request)
            )
    
    return redirect("usuarios:lista_roles")


def inicio(request):
    return render_to_response(
        'inicio.html', 
        locals(), 
        context_instance=RequestContext(request)
    )


@login_required
def index_view(request):
    return render_to_response('index.html', 
        locals(), 
        context_instance=RequestContext(request)
    )


def index(request):
    return render_to_response('index.html', 
        locals(),
        context_instance=RequestContext(request)
    )

"""La función captura los datos proporcionados por el usuario que intenta acceder al sistema, si los datos
de validación son correctos se hace uso de la función index_view la cual dirige a la página de inicio,
de lo contrario vuelve a la página de login y emite un mensaje de error."""
def login_view(request):
    if request.user.is_authenticated():
        return render_to_response('index.html', 
            locals(), 
            context_instance=RequestContext(request)
        )
    mensaje = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render_to_response('index.html', 
                    locals(), 
                    context_instance=RequestContext(request)
                )
            else:
                pass
        mensaje = 'El nombre usuario y/o la clave no son correctos'
    else:
        return render_to_response('login.html', 
            locals(), 
            context_instance=RequestContext(request)
        )
    return render_to_response('login.html', 
        locals(), 
        context_instance=RequestContext(request)
    )


"""La función finaliza la validación de un usuario logueado y lo dirige a la página de login, mediante esta misma
se puede hacer un login nuevamente al igual que la función login_view."""
def logout_view(request):
    logout(request)
    #messages.success(request, 'Desconectado satisfactoriamente')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render_to_response('index.html', 
                    locals(), 
                    context_instance=RequestContext(request)
                )
            else:
                pass
        mensaje = 'nombre o contrasena invalidos'
    return render_to_response('login.html', 
        locals(), 
        context_instance=RequestContext(request)
    )

