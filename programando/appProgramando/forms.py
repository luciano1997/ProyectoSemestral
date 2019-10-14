from django import forms
from .models import Curso, Alumno, Usuario


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombreCompleto', 'rut', 'email', 'telefono', 'region', 'comuna', 'fechaNacimiento', 'tipoVivienda', ]

        labels =   {'nombreCompleto':'nombreCompleto', 'rut':'rut', 'email':'email', 'telefono':'telefono', 'region':'region', 'comuna':'comuna', 'fechaNacimiento':'fechaNacimiento', 'tipoVivienda':'tipoVivienda' }
        widgets =  {'nombreCompleto': forms.TextInput(attrs={'class': 'form-control'}),
                    'rut': forms.TextInput(attrs={'class': 'form-control'}),
                    'email': forms.TextInput(attrs={'class': 'form-control'}),
                    'telefono': forms.TextInput(attrs={'class':'form-comtrol'}),
                    'region': forms.TextInput(attrs={'class':'form-comtrol'}),
                    'comuna': forms.TextInput(attrs={'class':'form-comtrol'}),
                    'fechaNacimiento': forms.TextInput(attrs={'class':'form-comtrol'}),
                    'tipoVivienda': forms.TextInput(attrs={'class':'form-comtrol'}), }