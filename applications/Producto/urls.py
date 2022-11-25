from django.contrib import admin
from django.urls import path, re_path, include
from . import views


urlpatterns = [
    path(
        'producto/',
        views.Producto.as_view(),
        name='Pagina producto'
    )
]
