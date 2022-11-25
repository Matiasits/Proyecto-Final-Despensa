from django.contrib import admin
from django.urls import path, re_path, include
from . import views

app_name = 'producto_app' 

urlpatterns = [
    path(
        'productos/listado/',
        views.ProductoListView.as_view(),
        name='Lista de Productos',
    ),
    path(
        'productos/busqueda/',
        views.ProductoSearch.as_view(),
        name='Busqueda de Productos',
    ),
    path(
        'productos/detalles/<pk>/', #se detalla que registro segun su clave primaria desea detallar
        views.ProductoDetalles.as_view(),
        name='Detalles de Productos',
    ),
    path(
        'productos/create/',
        views.ProductoCreateView.as_view(),
        name='Creacion de Productos',
    ),  
    path(
        'productos/update/<pk>/', #se detalla que registro segun su clave primaria desea actualizar
        views.ProductoUpdateView.as_view(),
        name='Modificar Productos'
    ),
    path(
        'productos/delete/<pk>/',
        views.ProductoDeleteView.as_view(),
        name='Borrar Productos'
    ),
]