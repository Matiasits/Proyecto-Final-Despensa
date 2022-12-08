from django.contrib import admin
from django.urls import path, re_path, include
from . import views 

app_name = 'proveedor_app' 

urlpatterns = [
    path(
        'inicio/',
        views.Home.as_view(),
        name='inicio'
    ),
    path(
        'proveedor/detalles/<pk>/',
        views.ProveedorDetalles.as_view(),
        name='Detalles de proveedor'
    ),
    path(
        'proveedor/create/',
        views.ProveedorCreateView.as_view(),
        name='Creacion de proveedor'
    ),
    path(
        'proveedor/update/<pk>/',
        views.ProveedorUpdateView.as_view(),
        name='Modificar proveedor'
    ),
    path(
        'proveedor/delete/<pk>/',
        views.ProveedorDeleteView.as_view(),
        name='Borrar proveedor'
    ),
    path(
        'login/',
        views.LoginUser.as_view(),
        name='login-proveedor'
    ),
    path(
        'proveedor/panel/',
        views.Panel.as_view(),
        name='panel-proveedor'
    ),
    path(
        'proveedor/logout/',
        views.LogoutView.as_view(),
        name='logout-proveedor'
    ),
    path(
        'proveedor/ordenar/identificador',
        views.ProveedorIdentificador.as_view(),
        name='proveedor-identificador'
    ),
    path(
        'proveedor/ordenar/nombre',
        views.ProveedorNombre.as_view(),
        name='proveedor-nombre'
    ),
    path(
        'proveedor/ordenar/rubro',
        views.ProveedorRubro.as_view(),
        name='proveedor-rubro'
    ),
    
    path(
        'proveedor/api',
        views.ProveedorListApiView.as_view(),
        name='api-proveedor'
    ),
]