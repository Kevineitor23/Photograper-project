from django import forms
from igles.models import Usuarios, Contacto

"""FORMULARIO DE BUSQUEDA API PIXELS"""
class UsuariosForm(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = ['name', 'dificultad']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder' : 'My Projects',
            })
        }
 


class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'placeholder' : 'Your name'}),
            'motivo': forms.Textarea(attrs={'placeholder': 'Contact'}),
            }




