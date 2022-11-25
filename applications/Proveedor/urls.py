from django.contrib import admin
from django.urls import path, re_path, include
from . import views 


urlpatterns = [
    path(
        'proveedores/inicio/',
        views.Inicio.as_view(),
        name='Pagina proveedor'
    ),
    path(
        'proveedores/listado/',
        views.ProveedorListView.as_view(),
        name='Lista de Proveedores'
    ),
    path(
        'proveedores/busqueda/',
        views.ProveedorSearch.as_view(),
        name='Busqueda de Proveedores'
    ),
    path(
        'proveedores/detalles/',
        views.ProveedorDetailView.as_view(),
        name='Detalles de Proveedores'
    ),
]