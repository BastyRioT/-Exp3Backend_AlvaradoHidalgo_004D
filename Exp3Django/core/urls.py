from django.urls import path
from .views import inicio, galeria, datos, form_registro

urlpatterns = [
    path('', inicio, name="inicio"),
    path('inicio.html', inicio, name="inicio"),
    path('galeria.html', galeria, name="galeria"),
    path('datos.html', datos, name="Datos"),
    path('form_registro.html', form_registro, name="registro"),
]
