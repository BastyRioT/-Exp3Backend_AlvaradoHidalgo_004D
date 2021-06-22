from .forms import RegistroForm
from django.shortcuts import render, redirect
from .models import Registro
# Create your views here.


def inicio(request):

    return render(request, 'inicio.html')


def galeria(request):

    return render(request, 'galeria.html')


def datos(request):

    registros = Registro.objects.all()

    return render(request, 'datos.html', {'registros': registros})


def form_registro(request):

    if request.method == 'POST':

        registro_form = RegistroForm(request.POST)

        if registro_form.is_valid():

            registro_form.save()

            return redirect('inicio')

    else:

        registro_form = RegistroForm()

    return render(request, 'form_registro.html', {'registro_form': registro_form})


def mod_registro(request, id):

    registro = Registro.objects.get(usuario=id)

    datos = {

        'form': RegistroForm(instance=registro)

    }

    if request.method == 'POST':

        formulario = RegistroForm(data=request.POST, instance=registro)

        if formulario.is_valid:

            registro.delete()

            formulario.save()

            return redirect('datos')

    return render(request, 'mod_registro.html', datos)
