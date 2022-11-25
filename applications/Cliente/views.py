from django.shortcuts import render
# Create your views here.
from django.views.generic import (
    ListView,
    DeleteView,
    CreateView,
    TemplateView,
    UpdateView,
    DetailView
)

from .models import Cliente
class Cliente(TemplateView):
    template_name = "inicio.html"


class ClienteListView(ListView):
    model = Cliente
    template_name = "cliente/listado.html"
    ordering = "dni"
    context_object_name = "clientes"


class ClienteListView(ListView):
    model = Cliente
    template_name = "cliente/busqueda.html"
    ordering = "dni"        #ordenamos segun el criterio que queramos
    context_object_name = "clientes"    #los objetos que las vistas mandan al template para ver clioentes tienen nombres por defecto, con esto le asignamos un nombre

def get_queryset(self):
    palabra_clave = self.request.GET.get('kword','')
    lista = Cliente.objects.filter(
        apellido__icontains = palabra_clave
    )
    return lista