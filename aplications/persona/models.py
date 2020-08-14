from django.db import models
from ckeditor.fields import RichTextField
from aplications.departamento.models import Departamento

# Create your models here.

class Habilidades(models.Model):
    habilidad=models.CharField(("Habilidad"), max_length=50)#si lo dejasmos asi el campo es obligatorio
    #son varias habilidades una para muchos
    class meta:
        verbose_name='Habilidad'
        verbose_name_plural = 'Habilidades Empleado'
    
    def __str__(self):
        return str(self.id) + '-' + self.habilidad#aqui es donde regresa la habilidad y la guarda en la vase de datos

class Empleado(models.Model):
#odelo para la tabla empleado
    JOBS_CHOICES=(
        ('0', 'CONTADOR'),
        ('1', 'ADMINISTRADOR'),
        ('2', 'ECONOMISTA'),
        ('3', 'OTRO'),#ESTO SE VA A GUARDAR Y SE MANDARA A LLAMAR EN LA LINEA JOB
    )
    first_name = models.CharField('nombres', max_length=50)
    last_name = models.CharField('apellido', max_length=50)
    full_name = models.CharField('nombres completo', max_length=120, blank=True)#dice que o es necesario
        
    
    #MODELO PARA TABLA DE EMPLEADO
    job = models.CharField('Trabajo', max_length=1, choices=JOBS_CHOICES)#aqui se crea un campo selccionable con las opciones rejistradas del 0 al 3 
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)#relacion directa de uno a muchos de departamento a empleados
    avatar = models.ImageField(upload_to='empleado', blank=True, null=True)#aqui carga las imagenes pero en upload se cargaran las imagenes buscara lo empleado y si no lo encuentra lo creara
    habilidades = models.ManyToManyField(Habilidades)#aqui se relaciona la tabla de 
    hoja_vida= RichTextField(blank=True)#aqui sirve para que apareece un recudro grande para editar el texto se installa en apps y en entorno virtual

    class Meta:
        verbose_name='Mi Empleadp'
        verbose_name=_plural='Empleados de la empresa'
        ordering=['-first_name','last_name']
        unique_together=['first_name','departamento']



    def __str__(self):
        return str(self.id) + '-' + self.first_name + '-' + self.last_name#CON ESTA LINEA RETORNA LOS VALORES AGREGADOS Y LOS GUARDA CUANDO LE DAS SALVAR  HABILIDAD NAME ETC SI NO DARA ERROR
    #image = models.ImageField(, upload_to=None, height_field=None, width_field=None, max_length=None)  #se ndecesita una base de datos mejor no la de defeto
