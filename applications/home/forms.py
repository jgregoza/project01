import imp
from turtle import width
from django import forms

from .models import Prueba

class PruebaForm(forms.ModelForm):
    """Form definition for Prueba."""

    class Meta:
        """Meta definition for Pruebaform."""

        model = Prueba
        fields = ('titulo', 'subtitulo', 'cantidad')
        widgets = {
            'titulo': forms.TextInput(attrs={'placeholder': 'ingrese un titulo'})
        }

    def clean_cantidad(self):   # redefenir metodo para realizar una validacion de un campo en el form
            cantidad = self.cleaned_data.get('cantidad')    # recupera el valor en el campo
            if cantidad < 10:   # realiza la validacion
                raise forms.ValidationError('Ingrese un numero mayor a 10') # msg de validacion

            return cantidad
