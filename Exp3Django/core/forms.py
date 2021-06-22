from django import forms
from django.forms import ModelForm
from .models import Registro


class RegistroForm(ModelForm):

    class Meta:
        model = Registro
        fields = ['correo', 'usuario', 'contraseña', 'fchnac']

        labels = {
            'correo': 'Correo Electronico ',
            'usuario': 'Usuario ',
            'contraseña': 'Contraseña ',
            'fhnac': 'Fecha de Nacimiento ',

        }
        widgets = {
            'correo': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'correo',
                    'name': 'email',
                    'placeholder': 'Ejemplo@ejemplo.cl'
                }
            ),
            'usuario': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'usuario',
                    'name': 'usuario',
                    'placeholder': 'Usuario123'
                }
            ),
            'contraseña': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'password',
                    'name': 'password',
                    'placeholder': 'Minimo 6 caracteres'
                }
            ),
            'fchnac': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'id': 'fchnac',
                    'name': 'fecha',
                    'min': '1900-01-01',
                    'placeholder': '1900-01-01'
                }
            )
        }
