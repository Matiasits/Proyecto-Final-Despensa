from django.contrib import admin
from django.urls import path, re_path, include
from . import views 

app_name = 'proveedor_app' 

urlpatterns = [
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
        'proveedores/detalles/<pk>/',
        views.ProveedorDetailView.as_view(),
        name='Detalles de Proveedores'
    ),
    path(
        'proveedores/create/',
        views.ProveedorCreateView.as_view(),
        name='Creacion de Proveedores'
    ),
    path(
        'proveedores/update/<pk>/',
        views.ProveedorUpdateView.as_view(),
        name='Modificar Proveedores'
    ),
    path(
        'proveedores/delete/<pk>/',
        views.ProveedorDeleteView.as_view(),
        name='Borrar Proveedores'
    ),
]