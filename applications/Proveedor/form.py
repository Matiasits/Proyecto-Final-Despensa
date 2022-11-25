#Formulario para crear
from django import forms
from.models import Proveedor

class ProveedorForm(forms.ModelForm):
    """Form definition for Cliente."""

    class Meta:
        """Meta definition for Clienteform."""

        model = Proveedor
        fields = ('identificador',
                  'nombre',
                  'rubro',
                  )
        widgets = {
            #'campo' : forms.CheckboxSelectMultiplePlace() #sirve para seleccionar varios valores 
        }