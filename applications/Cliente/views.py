from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, HttpResponse
from .models import Cliente
from .form import LoginForm, ClienteForm
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
    template_name = 'cliente/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('cliente_app:user-panel')
    
    def form_view(self, form):
        user = authenticate(
            username = form.cleaned_data['username'],
            password = form.cleaned_data['password']
            )
        login(self.request, user)
        return super(LoginUser, self).form_valid(form)

class Panel(LoginRequiredMixin, TemplateView):
    template_name = 'cliente/panel.html'
    login_url = reverse_lazy('cliente_app:user-login')
    
class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(
            reverse(
                'cliente_app:user-login'
            )
        )


############################ VIEWS ####################################
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
    
    
class ClienteUpdateView(UpdateView):    #ACTUALIZACION
    model = Cliente
    template_name = "cliente/update.html"
    form_class = ClienteForm
    success_url = reverse_lazy('cliente_app:Lista de Clientes')
    

class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = "cliente/delete.html"
    success_url = reverse_lazy('cliente_app:Lista de Clientes')

