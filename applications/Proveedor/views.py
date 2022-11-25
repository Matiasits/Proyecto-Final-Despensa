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

class Proveedor(TemplateView):
    template_name = "inicio1.html"