from django.contrib import admin
from django.urls import path, re_path, include
from . import views 


urlpatterns = [
    path(
        'proveedor/',
        views.Proveedor.as_view(),
        name='Pagina proveedor'
    )
]