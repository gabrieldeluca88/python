from django import forms
from .models import Cliente, Modelo, Auto

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'pais_origen']

class ModeloForm(forms.ModelForm):
    class Meta:
        model = Modelo
        fields = ['nombre', 'cliente']

class AutoForm(forms.ModelForm):
    class Meta:
        model = Auto
        fields = ['cliente', 'modelo', 'año', 'color']

class BuscarForm(forms.Form):
    query = forms.CharField(label='Buscar', max_length=100)
