from django.contrib import admin
from django.urls import path, re_path, include
from . import views

app_name = 'inicio_app'

urlpatterns = [
                path(
                    '',
                    views.Home.as_view(),
                    name='home'
                ),    
                path(
                    'inicio/',
                    views.Home.as_view(),
                    name='inicio'
                ),    
                path(
                    'apiPrueba/',
                    views.Api.as_view(),
                    name='api'
                ),    
]
