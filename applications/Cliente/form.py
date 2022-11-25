#Formulario para crear
from django import forms
from.models import Cliente

class ClienteForm(forms.ModelForm):
    """Form definition for Cliente."""

    class Meta:
        """Meta definition for Clienteform."""

        model = Cliente
        fields = ('apellido',
                  'nombre',
                  'dni',
                  )
        widgets = {
            #'campo' : forms.CheckboxSelectMultiplePlace() #sirve para seleccionar varios valores 
        }