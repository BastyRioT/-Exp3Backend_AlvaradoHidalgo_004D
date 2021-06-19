from django.shortcuts import render

# Create your views here.


def inicio(request):
    nombre = 'Claudia Andrea'

    return render(request, 'inicio.html', context={'nombre_usuario':nombre})


def galeria(request):

    return render(request, 'galeria.html')
