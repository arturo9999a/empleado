from django.contrib import admin
from . models import Empleado, Habilidades
# Register your models here.


admin.site.register(Habilidades)


class EmpleadoAdmin(admin.ModelAdmin):
    list_display=(
        'id',#estos son los campos que aparecen en el administrador de django aparecen en tabla 
        'first_name',
        'last_name',
        'departamento',
        'job',
        'full_name',
    )

    def full_name(self, obj):#con esta funcion se junrtaran el nombre y apellido para mostrarlo en una columna deladministrador de django
        print((obj.first_name))
        return obj.first_name + ' _ ' +obj.last_name



    search_fields=('first_name',)#con esto se hace un buscador para buscar en los nombres o datos se agrega como lo busques en las comillas simples como se ve
    list_filter=('departamento', 'job','habilidades',)#aparecera un cuadrito llamado filter con esto se filtra ahora si buscas solo podras buscar las areas y te apareceram los que pertenecen a ellas
    filter_horizontal=('habilidades',)#esto es para buscar las abilidades)
#con estas lineas hacemos que en el administrador de django nos muestre todo lo que pedimos los 4 
#sin esto solo daria menos informacion y con esto nos dara los 4 campos que le indicamos

admin.site.register(Empleado, EmpleadoAdmin)
#con esta linea activamos en el admin de django para que ahora lo muestre
#primero se llama el campo de donde estan y despues los atributos que creamos

