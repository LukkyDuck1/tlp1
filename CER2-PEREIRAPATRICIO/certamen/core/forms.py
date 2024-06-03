from django import forms 
from .models import propuesta

class Form_propuesta(forms.ModelForm):
    class Meta:
        model = propuesta
        fields = ['nombre','descripcion','patrocinio']

class editar_propuesta(forms.ModelForm):
    class Meta:
        model = propuesta
        fields= ['nombre','descripcion','patrocinio']