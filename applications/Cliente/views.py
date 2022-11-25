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
    template_name = "cliente.html"
    ordering = "dni"
    context_object_name = "clientes"
    
