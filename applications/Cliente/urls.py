from django.contrib import admin
from django.urls import path, re_path, include
from . import views

app_name = 'cliente_app' 

urlpatterns = [
    path(
        'clientes/listado/',
        views.ClienteListView.as_view(),
        name='Lista de Clientes',
    ),
    path(
        'clientes/busqueda/',
        views.ClienteSearch.as_view(),
        name='Busqueda de Clientes',
    ),
    path(
        'clientes/detalles/<pk>/', #se detalla que registro segun su clave primaria desea detallar
        views.ClienteDetalles.as_view(),
        name='Detalles de Clientes',
    ),
    path(
        'clientes/create/',
        views.ClienteCreateView.as_view(),
        name='Creacion de Cliente',
    ),  
    path(
        'clientes/update/<pk>/', #se detalla que registro segun su clave primaria desea actualizar
        views.ClienteUpdateView.as_view(),
        name='Modificar Cliente'
    ),
    path(
        'clientes/delete/<pk>/',
        views.ClienteDeleteView.as_view(),
        name='Borrar Cliente'
    ),
    path(
        'clientes/login/',
        views.LoginUser.as_view(),
        name='login-user'
    ),
    path(
        'clientes/panel/',
        views.Panel.as_view(),
        name='panel-cliente'
    ),
]