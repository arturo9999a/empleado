from django.shortcuts import render
from django.views.generic import (
    TemplateView, 
    ListView,
    CreateView
    )
from .models import Prueba
from .forms import PruebaForm
# Create your views here.



class PruebaView(TemplateView):
    template_name='home/prueba.html'
    #va  con minnuscula como se muestra si no dara el error de que no reconoce el template_name


class ResumenFoundationView(TemplateView):
    template_name = "home/resumen-fundation.html"



class PruebaListView(ListView):
    template_name = "home/lista.html"
    context_object_name='listaNUMEROS'
    queryset = ['1','10','20','30']
    

class ListaPrueba(ListView):
    template_name = "home/lista_prueba.html"
    model= Prueba#haxce una consulta de los rejistros al modelo prueba
    context_object_name='lista'

 
class PruebaCreateView(CreateView):
    model = Prueba
    template_name = "home/add.html"
    form_class= PruebaForm
    success_url = '/'
    #esto se usa para decir que aparecera ene el navegador como campos
    #utilizando la lapabra form crea las ccolumnas para ingresar datos automaticamente
    #y ya no es necesario crear los capos cada uno para eso see usa form y utiliza esas 4 sentencias

 