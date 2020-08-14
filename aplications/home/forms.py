from django import forms
from .models import Prueba

class PruebaForm(forms.ModelForm):
    
    class Meta:
        model = Prueba
        fields = (
            'titulo',
            'subtitulo',
            'cantidad',
            
        )
        widgets={

            'titulo': forms.TextInput(
                attrs ={
                    'placeholder': 'ingrese texto'
                }
            )

        }




    def clean_cantidad(self):
        cantidad= self.cleaned_data['cantidad']#con esto se validara el valor que no sea mayor que
        if cantidad < 10:#que solo sea mayor o dara error
            raise forms.ValidationError('ingrse un numero mayor a dies')#este lo mostrara si no es 10 o mayor
        return cantidad





    


