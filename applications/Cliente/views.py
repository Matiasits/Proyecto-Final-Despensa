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

class Inicio(TemplateView):
    template_name = "cliente/inicio.html"


class ClienteListView(ListView):
    model = Cliente
    template_name = "cliente/listado.html"
    ordering = "dni"
    context_object_name = "clientes"


class ClienteSearch(ListView):
    model = Cliente
    template_name = "cliente/busqueda.html"
    ordering = "dni"        #ordenamos segun el criterio que queramos
    context_object_name = "clientes"    #los objetos que las vistas mandan al template para ver clioentes tienen nombres por defecto, con esto le asignamos un nombre

    def get_queryset(self):
        #definimos variables donde obtendremos los request
        lastname = self.request.GET.get('lastname','')
        name = self.request.GET.get('name','')
        dni = self.request.GET.get('dni','')
        
        #del model Cliente filtramos los atributos que necesitamos
        lista = Cliente.objects.filter(
            apellido__icontains = lastname,
            nombre__icontains = name,
            dni__icontains = dni
        )
        
        return lista