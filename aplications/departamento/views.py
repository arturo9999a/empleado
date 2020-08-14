from django.shortcuts import render
from django.views.generic.edit import FormView # con esto importas y trabaja con mas de un modelo
from .forms import NewDepartamentoForm
from aplications.persona.models import Empleado
from .models import Departamento

from django.views.generic import ListView

class DepartmanetoListView(ListView):
    model=Departamento
    template_name = 'departamento/lista.html'
    context_object_name='departamentos'

class NewDepartamentoView(FormView):
    template_name = 'departamento/new_departamento.html'
    form_class= NewDepartamentoForm
    success_url =  '/'#dirije a pagina cuando los datos son correctos



    def form_valid(self, form):
        
        print('****************estamos en el form valid*************')

        depa = Departamento(
            name=form.cleaned_data['departamento'],
            shor_name=form.cleaned_data['shorname'],

        )#con esta instancia se crea para poder crear o modificar gracias a la instancia
        depa.save()#con esto ya esta creado y se indico que se guardo
        nombre = form.cleaned_data['nombre']
        apellido = form.cleaned_data['apellidos']#si se le quita la S da error
        Empleado.objects.create(
            first_name=nombre,
            last_name=apellido,
            job='1',
            departamento= depa
        )#para jhacer rejistro se usa la orm de django objects para rejistrar o modificar algo
        return super(NewDepartamentoView, self).form_valid(form)