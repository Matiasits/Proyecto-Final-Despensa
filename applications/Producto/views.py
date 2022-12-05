from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, HttpResponse
from .models import Producto
from .form import LoginForm, ProductoForm
from rest_framework.generics import ListAPIView
from .serializer import ProductoSerializer
from django.views.generic import (
    View,
    ListView,
    DeleteView,
    CreateView,
    TemplateView,
    UpdateView,
    DetailView
)
from django.views.generic.edit import (
    FormView
)

############################ LOGIN ####################################
class LoginUser(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = reverse_lazy('producto_app:panel-producto')
    context_object_name = 'login'
    
    def form_valid(self, form):
        user = authenticate(
            username = form.cleaned_data['username'],
            password = form.cleaned_data['password']
            )
        login(self.request, user)
        return super(LoginUser, self).form_valid(form)


class Panel(LoginRequiredMixin, ListView):
    model = Producto
    template_name = 'producto/panel.html'
    context_object_name = 'productos'
    paginate_by = 5
    login_url = reverse_lazy('producto_app:login-producto')

    def get_queryset(self):
        #definimos variables donde obtendremos los request

        dato = self.request.GET.get('dato','')
        #del model Producto filtramos los atributos que necesitamos
        lista = Producto.objects.filter(identificador__icontains = dato) | Producto.objects.filter(nombre__icontains = dato) | Producto.objects.filter(tipo__icontains = dato)
        
        return lista
class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(
            reverse(
                'producto_app:login-producto'
            )
        )

############################ VIEWS ####################################


class ProductoDetalles(LoginRequiredMixin,DetailView):    
    model = Producto
    template_name = "producto/detalles.html"      
    context_object_name = "detalle"
    login_url = reverse_lazy('producto_app:login-producto')


class ProductoCreateView(CreateView):    #CREACION LoginRequery
    model = Producto
    template_name = "producto/create.html"
    form_class = ProductoForm
    success_url = reverse_lazy('producto_app:panel-producto') #una vez agregado, vuelve hacia la pag que le pasemos
    login_url = reverse_lazy('producto_app:login-producto')


class ProductoUpdateView(LoginRequiredMixin,UpdateView):  #BUSQUEDA SEGUN CRITERIO
    model = Producto
    template_name = 'producto/update.html'
    context_object_name = 'productos'    #los objetos que las vistas mandan al template para ver clioentes tienen nombres por defecto, con esto le asignamos un nombre
    success_url = reverse_lazy('producto_app:panel-producto')
    login_url = reverse_lazy('producto_app:login-producto')

   

class ProductoDeleteView(LoginRequiredMixin,DeleteView,DetailView):  
    model = Producto
    template_name = "producto/delete.html"
    context_object_name = "delete_detail"
    success_url = reverse_lazy('producto_app:panel-producto')
    login_url = reverse_lazy('producto_app:login-producto')

############################ VIEWS DE ORDEN ####################################

class ProductoIdentificador(LoginRequiredMixin,ListView):
    model = Producto
    template_name = "producto/panel.html"
    ordering = 'identificador'
    paginate_by = 5
    context_object_name = "productos"    #los objetos que las vistas mandan al template para ver clioentes tienen nombres por defecto, con esto le asignamos un nombre
    login_url = reverse_lazy('producto_app:login-producto')


class ProductoNombre(LoginRequiredMixin,ListView):
    model = Producto
    template_name = "producto/panel.html"
    ordering = 'nombre'
    paginate_by = 5
    context_object_name = "productos"    #los objetos que las vistas mandan al template para ver clioentes tienen nombres por defecto, con esto le asignamos un nombre
    login_url = reverse_lazy('producto_app:login-producto')


class ProductoTipo(LoginRequiredMixin,ListView):
    model = Producto
    template_name = "producto/panel.html"
    ordering = 'tipo'
    paginate_by = 5
    context_object_name = "productos"    #los objetos que las vistas mandan al template para ver clioentes tienen nombres por defecto, con esto le asignamos un nombre
    login_url = reverse_lazy('producto_app:login-producto')
    
class ProductoMarca(LoginRequiredMixin,ListView):
    model = Producto
    template_name = "producto/panel.html"
    ordering = 'marca'
    paginate_by = 5
    context_object_name = "productos"    #los objetos que las vistas mandan al template para ver clioentes tienen nombres por defecto, con esto le asignamos un nombre
    login_url = reverse_lazy('producto_app:login-producto')


############################ API VIEW ####################################


class ProductoListApiView(ListAPIView):

    serializer_class = ProductoSerializer

    def get_queryset(self):
        return Producto.objects.all()