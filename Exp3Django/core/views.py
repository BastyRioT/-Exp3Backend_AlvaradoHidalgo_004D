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

    datos = {
        'registros': registros
    }

    return render(request, 'datos.html', datos)


def form_registro(request):

    if request.method == 'POST':

        registro_form = RegistroForm(request.POST)

        if registro_form.is_valid():

            registro_form.save()

            return redirect('home')

    else:

        registro_form = RegistroForm()

    return render(request, 'form_registro.html', {'registro_form': registro_form})
