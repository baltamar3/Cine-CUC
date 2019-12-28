from django import forms
from .models import Funcion
from django.forms.widgets import SelectDateWidget

class FuncionForm(forms.ModelForm):
    fecha_inicio = forms.DateTimeField(widget=SelectDateWidget())
    fecha_fin  = forms.DateTimeField(widget=SelectDateWidget())
    class Meta:
        model = Funcion
        fields = (
            'pelicula',
            'fecha_inicio',
            'fecha_fin',
            'lugar',
            'direccion',
            'cupos'
        )