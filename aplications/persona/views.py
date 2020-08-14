from . forms import EmpleadoForm

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,#listar los elementos
    DetailView,
    CreateView,#para ingresar usuario y registrarlo
    TemplateView,#mostrar una template estatico o editar o eliminar desde el html 
    UpdateView,#actualizar datos de la base de datos o modificarlos
    DeleteView#para eliminar datos de la base de datos del proyecto

)


from .models import Empleado


class InicioView(TemplateView):
    #vista que carga la pagina de inicio 
    template_name = 'inicio.html'

class ListaAllEmpleados(ListView):
    template_name= 'persona/list_all.html'
    paginate_by = 5  #con esto le dices cuantos datos quieres que te mande


    def get_queryset(self):
    
        palabra_clave = self.request.GET.get("kword", '')   #aqui se interceptan las solicitudes del navegador

        lista= Empleado.objects.filter(
            first_name__icontains=palabra_clave#con esto accede al atributo de nombre y al agregar una pabra al buscador la busca en nombre y regresa el resultado en la tabla
            
        )
        #print('lista resultado', lista, '**********************')#muetsra la lista en consola
        return lista#con esta vista se recupera en la tabla de los datos




class ListaAEmpleadosAdmin(ListView):
    template_name= 'persona/list_empleados.html'
    paginate_by = 10  #con esto le dices cuantos datos quieres que te mande
    ordering='first_name'
    context_object_name='empleados'#con esto accederemos a los datos desde el html poniendo empleados
    model=Empleado


class ListaByeAreEmpleados(ListView):
    template_name= 'persona/list_bye_area.html'
    #queryset= Empleado.objects.filter(   #esta es la peor forma de hacer listas 
    #    departamento__shor_name='conta'#con esto llama al atributo con la llave foranea
    #se manda a traer el nombre del departamento con 2 guienes bajos _ _ y primero la clase despues el nombre del segundo atributo ya que tiene una llave foranea
    context_object_name='empleados'#para poder acceder a los atributos desde este nombre en el html
    #)#con esto me regresa la lista de lo que pida

    def get_queryset(self):
        area=self.kwargs['shorname']#aquie recive los argumentos que se escriben en la url por eso se configuro en urls
        lista= Empleado.objects.filter(
            departamento__shor_name=area
        )
        
        return lista



class LiaEmpleadosBykword(ListView):
    #lista de empleados por palabra clave
    template_name = 'persona/bye_kword.html'
    context_object_name= 'empleados'# este sera el nombre con el cual se accedr A LA lista creada

    def get_queryset(self):
        print('$$$$$$$$$$$')
        palabra_clave = self.request.GET.get("kword", '')   #aqui se interceptan las solicitudes del navegador

        lista= Empleado.objects.filter(
            first_name=palabra_clave
        )
        print('lista resultado', lista)
        return lista


class ListaHabilidadesEmpleado(ListView):
    template_name= 'persona/habilidades.html'
    context_object_name = 'habilidades'

    def get_queryset(self):
        empleado= Empleado.objects.get(id=5)#con esta linea agregando get solo se pide un inico dato de la basae de datos por eso se pide el id
        #print(empleado.habilidades.all()) # con esto mostraba el valor en la consola
        return empleado.habilidades.all()#ahora mandamos los valores en consola para que el html los llame


class EmpleadoDetailView(DetailView): #toda vista bsada en clase trabaja con tmeplate
    model = Empleado
    template_name = "persona/detail_empleado.html"


class SuccessView(TemplateView):
    template_name = "persona/success.html"



class EmpleadoCreateView(CreateView):#crear y editar formularios vista generica
    model = Empleado#el modelo por que se agregaran mas eomleados
    template_name = "persona/add.html"
   #fields = [ 'first_name', 'last_name', 'job' ] #aqui nos creara una estructura html
    #el fiels crea las cajas de texto para ingresar los tres valores que se piden arriba
  # ## fields = ('__all__')#con este all va a manndar a traer todos los atributos TODOS
    #A DIFERENCIA DEL ANTERIOR ERA UNO POR UNO A QUI MANDA A TRAER TODOS
    form_class = EmpleadoForm
   # fields= [
    #    'first_name',
     #   'last_name',
      #  'job',
       # 'departamento',
        #'habilidades',
        #'avatar',
    #]aqui se manda a traer dato por dato y no tod con __all__
    
    success_url = reverse_lazy ('persona_app:empleados_admin')#esto sirve para cuado se guarde se actualice la paguna
    def form_valid(self, form):#algo que seseda despues del guardado el foem valid intercepta los datos
        empleado = form.save()#con esto se almacena lo que se ingresa en el formulario de empleado
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name #se concatenan los dos datos 
        empleado.save()#con esto se guarda en la base de datos el valor full_name
        return super(EmpleadoCreateView, self).form_valid(form)#super para sobre escribir



        
class EmpleadoUpdateView(UpdateView):
    model = Empleado
    template_name = "persona/update.html"
    fields= [
        'first_name',
        'last_name',
        'job',
        'departamento',
        'habilidades',
    ]
    success_url = reverse_lazy ('persona_app:empleados_admin')#esto sirve para cuado se guarde se actualice la paguna
    #logica del proceso
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print('*****************post******************')
        print(request.POST)
        print(request.POST['last_name'])#se manda a llamar el apellido de quien se actualice el nombre
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        print('******************valid*****************')
        return super(EmpleadoUpdateView, self).form_valid(form)




class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "persona/delete.html"
    success_url = reverse_lazy ('persona_app:empleados_admin')#esto sirve para cuado se guarde se actualice la paguna