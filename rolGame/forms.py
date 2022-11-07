from .models import *
from django import forms

class rol(forms.ModelForm):
    class Meta:
        model = juego_rol
        field = '__all__'

class name(forms.Form):
    class Meta:
        model = nameDb
        field = '__all__'
