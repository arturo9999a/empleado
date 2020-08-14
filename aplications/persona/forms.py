from django import forms

from . models import Empleado

class EmpleadoForm(forms.ModelForm):
#con esto se personalizaran estos campos de datos
    class Meta:
        model = Empleado
        fields = (
            'first_name',
            'last_name',
            'job',
            'departamento',
            'avatar',
            'habilidades',
        )
        #asi es como se edita los formularios desde forms
        widgets={

            'habilidades': forms.CheckboxSelectMultiple(
                
            )
        }