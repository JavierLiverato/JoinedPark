from django.conf.urls import include, url

urlpatterns = [    
	url(r'^nuevo_usuario/$', 'usuarios.views.nuevo_usuario', name='nuevo_usuario'),
	url(r'^nuevo_rol/$', 'usuarios.views.nuevo_rol', name='nuevo_rol'),

	url(r'^lista_usuarios/$', 'usuarios.views.lista_usuarios', name='lista_usuarios'),
	url(r'^lista_roles/$', 'usuarios.views.lista_roles', name='lista_roles'),

	url(r'^actualizar_usuario/(?P<id>\d+)/$', 'usuarios.views.actualizar_usuario', name='actualizar_usuario'),
	url(r'^actualizar_rol/(?P<id>\d+)/$', 'usuarios.views.actualizar_rol', name='actualizar_rol'),

	url(r'^eliminar_usuario/(?P<id>\d+)/$', 'usuarios.views.eliminar_usuario', name='eliminar_usuario'),
	url(r'^eliminar_rol/(?P<id>\d+)/$', 'usuarios.views.eliminar_rol', name='eliminar_rol'),

	url(r'^inicio/$', 'usuarios.views.inicio', name='inicio'),
	url(r'^login_view/$', 'usuarios.views.login_view', name='login_view'),
    url(r'^index_view/$', 'usuarios.views.index_view', name='index_view'),
    url(r'^logout_view/$', 'usuarios.views.logout_view', name='logout_view'),
    

#	url(r'^profile/$', 'usuarios.views.update_profile', name='profile'),

]
