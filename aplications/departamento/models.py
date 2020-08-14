from django.db import models

# Create your models here.
class Departamento(models.Model):
    name = models.CharField('Nombre', max_length=50)#si le agrego blanck=true no sera obligatorio el campo
    shor_name = models.CharField('Nombre corto', max_length=20)#si le pongo unique= true solo sera un campo no se podra repetir
    anulate = models.BooleanField('anulado', default=False)#este solo dara campo de verdadero o falso asi es y se le aagraga un valor falso por eso se le cambia el valor
    
    class Meta:
        verbose_name= 'Mi Departamento'#EN ESTA SECCION SE CREA o se hacen los cambios de plural a singular en el administrador de django ya que son en plural 
        verbose_name_plural = 'Areas de la empresa'
        ordering = ['-name']#con esto se ordenan los datos de la clase
        unique_together = ('name', 'shor_name')# que no se rejistre atributo dos veces o que se repita no se repita


    def __str__(self):
        return str(self.id) + '-' + self.name + '-' + self.shor_name
