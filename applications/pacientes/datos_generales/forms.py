from tkinter import Widget
from django import forms
from applications.pacientes.datos_generales.models import Pacientes

class FormPacientes(forms.ModelForm):
    class Meta:
        model = Pacientes

        fields = ('codigo','nombre','email','sexo','fecha_nacimiento','escolaridad','tipo_sangre','estado_civil')

        widgets = {
            'codigo':forms.TextInput(
                attrs={
                    'placeholder':'Codigo'
                }
            ),
            'nombre':forms.TextInput(
                attrs={
                    'placeholder':'Nombre'
                }
            ),
            'email':forms.TextInput(
                attrs={
                    'placeholder':'Email'
                }
            ),
            'sexo': forms.TextInput(
                attrs={
                    'placeholder':'Sexo'
                }
            ),
            'fecha_nacimiento': forms.DateInput(
                attrs={
                    'placeholder':'Fecha de Nacimiento'
                }
            ),
            'escolaridad': forms.TextInput(
                attrs={
                    'placeholder':'Escolaridad'
                }
            ),
            'tipo_sangre': forms.TextInput(
                attrs={
                    'placeholder':'Tipo de Sangre'
                }
            ),
            'estado_civil': forms.TextInput(
                attrs={
                    'placeholder':'Estado Civil'
                }
            ),
        }