from django.urls import path
from .views import inicio, galeria, datos, form_registro, mod_registro, del_registro

urlpatterns = [
    path('', inicio, name="inicio"),
    path('galeria', galeria, name="galeria"),
    path('form_registro', form_registro, name="form_registro"),
    path('datos/', datos, name="datos"),
    path('mod_registro/<id>', mod_registro, name="mod_registro"),
    path('del_registro/<id>', del_registro, name="del_registro"),
]
