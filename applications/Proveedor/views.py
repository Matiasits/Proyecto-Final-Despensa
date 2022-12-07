from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, HttpResponse
from .models import Proveedor
from .form import LoginForm, ProveedorForm
from rest_framework.generics import ListAPIView
from .serializer import ProveedorSerializer
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
    success_url = reverse_lazy('proveedor_app:panel-proveedor')
    context_object_name = 'login'
    
    def form_valid(self, form):
        user = authenticate(
            username = form.cleaned_data['username'],
            password = form.cleaned_data['password']
            )
        login(self.request, user)
        return super(LoginUser, self).form_valid(form)


class Panel(ListView):
    model = Proveedor
    template_name = 'proveedor/panel.html'
    context_object_name = 'proveedor'
    paginate_by = 5

    
    def get_queryset(self):
        #definimos variables donde obtendremos los request
        
        dato = self.request.GET.get('dato','')
        #del model Proveedor filtramos los atributos que necesitamos
        lista = (
            Proveedor.objects.filter(identificador__icontains = dato) 
            | Proveedor.objects.filter(nombre__icontains = dato) 
            | Proveedor.objects.filter(rubro__icontains = dato)
                )
        return lista
    
class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(
            reverse(
                'proveedor_app:login-proveedor'
            )
        )

############################ VIEWS ####################################

class ProveedorDetalles(LoginRequiredMixin,DetailView):
    model = Proveedor
    template_name = "proveedor/detalles.html"
    context_object_name = "detalle"
    login_url = reverse_lazy('proveedor_app:login-proveedor')


class ProveedorCreateView(LoginRequiredMixin,CreateView):
    model = Proveedor
    template_name = "proveedor/create.html"
    form_class = ProveedorForm
    success_url = reverse_lazy('proveedor_app:panel-proveedor') #una vez agregado, vuelve hacia la pag que le pasemos
    login_url = reverse_lazy('proveedor_app:login-proveedor')


class ProveedorUpdateView(LoginRequiredMixin,UpdateView):
    model = Proveedor
    template_name = "proovedor/update.html"
    form_class = ProveedorForm
    success_url = reverse_lazy('proveedor_app:panel-proveedor') #una vez agregado, vuelve hacia la pag que le pasemos
    login_url = reverse_lazy('proveedor_app:login-proveedor')


class ProveedorDeleteView(LoginRequiredMixin,DeleteView,DetailView):
    model = Proveedor
    template_name = "proveedor/delete.html"
    context_object_name = 'delete_detail'
    success_url = reverse_lazy('proveedor_app:panel-proveedor') #una vez agregado, vuelve hacia la pag que le pasemos
    login_url = reverse_lazy('proveedor_app:login-proveedor')

############################ VIEWS DE ORDEN ####################################


class ProveedorIdentificador(LoginRequiredMixin,ListView):
    model = Proveedor
    template_name = "proveedor/panel.html"
    ordering = 'identificador'
    paginate_by = 5
    context_object_name = "proveedor"    #los objetos que las vistas mandan al template para ver clioentes tienen nombres por defecto, con esto le asignamos un nombre
    login_url = reverse_lazy('proveedor_app:login-proveedor')


class ProveedorNombre(LoginRequiredMixin,ListView):
    model = Proveedor
    template_name = "proveedor/panel.html"
    ordering = 'nombre'
    paginate_by = 5
    context_object_name = "proveedor"    #los objetos que las vistas mandan al template para ver clioentes tienen nombres por defecto, con esto le asignamos un nombre
    login_url = reverse_lazy('proveedor_app:login-proveedor')


class PRoveedorRubro(LoginRequiredMixin,ListView):
    model = Proveedor
    template_name = "proveedor/panel.html"
    ordering = 'rubro'
    paginate_by = 5
    context_object_name = "proveedor"    #los objetos que las vistas mandan al template para ver clioentes tienen nombres por defecto, con esto le asignamos un nombre
    login_url = reverse_lazy('proveedor_app:login-proveedor')
    

############################ API VIEW ####################################
class ProveedorListApiView(ListAPIView):

    serializer_class = ProveedorSerializer

    def get_queryset(self):
        return Proveedor.objects.all()