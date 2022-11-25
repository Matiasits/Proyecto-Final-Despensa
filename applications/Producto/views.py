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


from .models import Producto
from .form import ProductoForm
from django.urls import reverse_lazy


class ProductoListView(ListView):    #LISTADO
    model = Producto
    template_name = "producto/listado.html"      #UBICACION Y NOMBRE DEL TEMPLATE 
    ordering = "identificador"
    context_object_name = "productos"


class ProductoSearch(ListView):  #BUSQUEDA SEGUN CRITERIO
    model = Producto
    template_name = "producto/busqueda.html"
    ordering = "identificador"        #ordenamos segun el criterio que queramos
    context_object_name = "productos"    #los objetos que las vistas mandan al template para ver clioentes tienen nombres por defecto, con esto le asignamos un nombre

    def get_queryset(self):
        #definimos variables donde obtendremos los request
        identificador = self.request.GET.get('identificador','')
        name = self.request.GET.get('name','')
        tipo = self.request.GET.get('tipo','')
        marca = self.request.GET.get('marca','')
        
        #del model Producto filtramos los atributos que necesitamos
        lista = Producto.objects.filter(
            identificador__icontains = identificador,
            nombre__icontains = name,
            tipo__icontains = tipo,
            marcaProd_icontains = marca,
        )
        
        return lista


class ProductoDetalles(DetailView):  #DETALLES 
    model = Producto
    template_name = "producto/detalles.html"
    context_object_name = "detalle"


class ProductoCreateView(CreateView):    #CREACION LoginRequery
    model = Producto
    template_name = "producto/create.html"
    form_class = ProductoForm
    success_url = reverse_lazy('producto_app:Lista de Productos') #una vez agregado, vuelve hacia la pag que le pasemos


class ProductoUpdateView(UpdateView):    #ACTUALIZACION
    model = Producto
    template_name = "producto/update.html"
    form_class = ProductoForm
    success_url = reverse_lazy('producto_app:Lista de Productos')
    """
    def form_valid(self, form):
        cl = form.save(commit=False)
        cl.nombre_completo = f"{cl.nombre} {cl.apellido}"
        cl.save()
        return super(ClienteUpdateView,self).form_valid(form)    
    """


class ProductoDeleteView(DeleteView):
    model = Producto
    template_name = "producto/delete.html"
    success_url = reverse_lazy('producto_app:Lista de Productos')