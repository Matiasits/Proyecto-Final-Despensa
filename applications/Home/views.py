from django.shortcuts import render
from django.views.generic import TemplateView
from .services import anime

############################ HOME VIEW ####################################

class Home(TemplateView):
    template_name = 'home.html'
    
class Api(TemplateView):
    template_name = 'api.html'
    context_object_name = 'api_data'
    