#Formulario para crear
from django import forms
from.models import Cliente
from django.contrib.auth import authenticate

class ClienteForm(forms.ModelForm):
    """Form definition for Cliente."""

    class Meta:
        """Meta definition for Clienteform."""
        model = Cliente
        fields = (
                'nombre',
                'apellido',
                'dni',
                  )
        
############################ LOGIN ####################################
class LoginForm(forms.Form):
    username = forms.CharField(
        label = 'Usuario',
        required = True,
        widget = forms.TextInput(
            attrs = {
                'placeholder': 'usuario',
                'class' : 'form-control',
                'type' : 'text',
            }
        )
    )
    password = forms.CharField(
        label = 'Contraseña',
        required = True,
        widget = forms.PasswordInput(
            attrs = {
                'placeholder': 'contraseña',
                'class' : 'form-control',
                'type' : 'password',
            }
        )
    )
    

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        
        if not authenticate(username=username, password=password):
            raise forms.ValidationError("Los datos ingresados son incorrectos")

        return self.cleaned_data
        
"""
class ClienteForm(forms.ModelForm):
    
    class meta:
        
        model = Cliente
        fields = '__all__'
    

        model = Cliente
        fields = ('apellido',
                  'nombre',
                  'dni',
                  )
        widgets = {
            #'campo' : forms.CheckboxSelectMultiplePlace() #sirve para seleccionar varios valores 
        }
"""