from django.contrib import admin
from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path(
        'clientes/inicio/',
        views.Inicio.as_view(),
        name='Pagina cliente',
    ),
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
]