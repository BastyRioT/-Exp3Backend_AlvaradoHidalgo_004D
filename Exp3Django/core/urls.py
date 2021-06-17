from django.urls import path
from .views import inicio, galeria

urlpatterns = [
    path('', inicio, name="inicio"),

]
