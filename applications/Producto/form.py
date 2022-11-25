#Formulario para crear
from django import forms
from.models import Producto

class ProductoForm(forms.ModelForm):
    """Form definition for Cliente."""

    class Meta:
        """Meta definition for Clienteform."""

        model = Producto
        fields = ('identificador',
                  'nombre',
                  'tipo',
                  'marcaProd',
                  )
        widgets = {
            #'campo' : forms.CheckboxSelectMultiplePlace() #sirve para seleccionar varios valores 
        }