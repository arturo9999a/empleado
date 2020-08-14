from django.db import models

# Create your models here.

class Prueba(models.Model):
    titulo = models.CharField(max_length=100)#en esta linea indica el titulo que va hacer un titulo por eso usa charfield y el maximo que utilizara
    subtitulo = models.CharField( max_length=50)
    cantidad = models.IntegerField()#en este es numero ya que se usa integerrfield
    #todoesto se tranfosrmara por la omr de django para la base de datos aun que cambies de base de datos no cambia el codigo se encarga de eso la orm
    def __str__(self):
        return self.titulo +'' + self.subtitulo
         