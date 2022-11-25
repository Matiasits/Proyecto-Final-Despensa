from django.shortcuts import render
# Create your views here.
from django.views.generic import (
    ListView,
    DeleteView,
    CreateView,
    TemplateView,
    UpdateView,
    DetailView,
)

from .models import Proveedor
from .form import ProveedorForm
from django.urls import reverse_lazy


class ProveedorListView(ListView):
    model = Proveedor
    template_name = "proveedor/listado.html"
    ordering = "identificador"
    context_object_name = "proveedores"


class ProveedorSearch(ListView):
    model = Proveedor
    template_name = "proveedor/busqueda.html"
    ordering = "identificador"
    context_object_name = "proveedores"
    
    def get_queryset(self):
        #definimos variables donde obtendremos los request
        rubro = self.request.GET.get('rubro','')
        name = self.request.GET.get('name','')
        identificador = self.request.GET.get('identificador','')
        
        #del model Proveedor filtramos los atributos que necesitamos
        lista = Proveedor.objects.filter(
            identificador__icontains = identificador,
            nombre__icontains = name,
            rubro__icontains = rubro
        )
        
        return lista


class ProveedorDetailView(DetailView):
    model = Proveedor
    template_name = "proveedor/detalles.html"
    context_object_name = "detalle"


class ProveedorCreateView(CreateView):
    model = Proveedor
    template_name = "proveedor/create.html"
    form_class = ProveedorForm
    success_url = reverse_lazy('proveedor_app:Lista de Proveedores') #una vez agregado, vuelve hacia la pag que le pasemos
    

class ProveedorUpdateView(UpdateView):
    model = Proveedor
    template_name = "proovedor/update.html"
    form_class = ProveedorForm
    success_url = reverse_lazy('proveedor_app:Lista de Proveedores') #una vez agregado, vuelve hacia la pag que le pasemos
    

class ProveedorDeleteView(DeleteView):
    model = Proveedor
    template_name = "proveedor/delete.html"
    form_class = ProveedorForm
    success_url = reverse_lazy('proveedor_app:Lista de Proveedores') #una vez agregado, vuelve hacia la pag que le pasemos
    