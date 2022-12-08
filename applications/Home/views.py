from django.shortcuts import render
from django.views.generic import TemplateView


############################ HOME VIEW ####################################

class Home(TemplateView):
    template_name = 'home.html'
    