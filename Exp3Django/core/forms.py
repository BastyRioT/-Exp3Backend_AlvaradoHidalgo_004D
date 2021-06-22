from Exp3Django.settings import DATABASES
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
                    'datafield': 'ejemplo@ejemplo.cl'
                }
            ),
            'usuario': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'usuario',
                    'name': 'usuario',
                    'datafield': 'usuario123'
                }
            ),
            'contraseña': forms.PasswordInput(
                attrs={
                    'class': 'form-control',
                    'id': 'password',
                    'name': 'password'
                }
            ),
            'fchnac': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'id': 'fchnac',
                    'name': 'fecha',
                    'min': '1900-01-01',
                    'datafield': '1900-01-01'
                }
            )
        }
