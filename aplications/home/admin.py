from django.contrib import admin

# Register your models here.

from . models import Prueba#asi se  importa la base de datos o el modelo que se creo como base de datos

admin.site.register(Prueba)#asi se importa la base de datos para poder visualizarla en el administrador de django
