from django.contrib import admin
from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path(
        'Inicio/',
        views.Cliente.as_view(),
        name='Pagina cliente'
    ),
    path(
        'clientes/',
        views.ClienteListView.as_view(),
        name='Lista de Clientes'
    )
]