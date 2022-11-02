from django import forms
from .models import Articulos, Iva, Categoria

class modelo_carta(forms.ModelForm):
    class Meta:
        model = Articulos
        fields = '__all__'
        labels = {
            'articulo': 'articulo',
            'categoria': 'categoria',

        }

class iva(forms.ModelForm):
    
    class Meta:
        model = Iva
        fields = '__all__'

class categoria(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'
