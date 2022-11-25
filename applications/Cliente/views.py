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
from .form import ClienteForm
from django.urls import reverse_lazy


class Inicio(TemplateView): #VISTA DE INICIO
    template_name = "cliente/inicio.html"


class ClienteListView(ListView):    #LISTADO
    model = Cliente
    template_name = "cliente/listado.html"      #UBICACION Y NOMBRE DEL TEMPLATE 
    ordering = "dni"
    context_object_name = "clientes"


class ClienteSearch(ListView):  #BUSQUEDA SEGUN CRITERIo
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

class ClienteDetalles(DetailView):  #DETALLES
    model = Cliente
    template_name = "cliente/detalles.html"
    context_object_name = "detalle"


class ClienteCreateView(CreateView):    #CREACION
    model = Cliente
    template_name = "cliente/create.html"
    form_class = ClienteForm
    success_url = reverse_lazy('cliente_app:Lista de Clientes') #una vez agregado, vuelve hacia la pag que le pasemos
    
    
    def form_valid(self, form):
        
        cl = form.save(commit=False)
        cl.nombre_completo = f"{cl.nombre} {cl.apellido}"
        cl.save()
        return super(ClienteCreateView, self).form_valid(form)


class ClienteUpdateView(UpdateView):    #ACTUALIZACION
    model = Cliente
    template_name = "cliente/update.html"
    form_class = ClienteForm
    success_url = reverse_lazy('cliente_app:Lista de Clientes')
    
    def form_valid(self, form):
        cl = form.save(commit=False)
        cl.nombre_completo = f"{cl.nombre} {cl.apellido}"
        cl.save()
        return super(ClienteUpdateView,self).form_valid(form)    
    

class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = "cliente/delete.html"
    success_url = reverse_lazy('cliente_app:Lista de Clientes')
