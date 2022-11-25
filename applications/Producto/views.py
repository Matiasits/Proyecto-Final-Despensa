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

from .models import Producto
class Producto(TemplateView):
    template_name = "inicio2.html"