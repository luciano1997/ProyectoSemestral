from django import forms
from .models import Curso, Alumno#, Usuario
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from rest_framework import routers, serializers, viewsets
#class UsuarioForm1(forms.ModelForm):
#    class Meta:
#        model = Usuario
#        fields = ['nombreCompleto', 'rut', 'email', 'telefono', 'region', 'comuna', 'fechaNacimiento', 'tipoVivienda', 'password' ]
#
#        labels =   {'nombreCompleto': 'Nombre Completo', 'rut': 'Rut', 'email': 'Email', 'telefono': 'Telefono', 'region': 'Region', 'comuna': 'Comuna', 'fechaNacimiento': 'Fecha De Nacimiento', 'tipoVivienda': 'Tipo de Vivienda', 'password':'password' }
#        widgets =  {'nombreCompleto': forms.TextInput(attrs={'class': 'form-control'}),
#                    'rut: ': forms.TextInput(attrs={'class': 'form-control'}),
#                    'email: ': forms.TextInput(attrs={'class': 'form-control'}),
#                    'telefono ': forms.TextInput(attrs={'class':'form-comtrol'}),
#                    'region ': forms.TextInput(attrs={'class':'form-comtrol'}),
#                    'comuna ': forms.TextInput(attrs={'class':'form-comtrol'}),
#                    'fechaNacimiento ': forms.TextInput(attrs={'class':'form-comtrol'}),
#                    'tipoVivienda ': forms.TextInput(attrs={'class':'form-comtrol'}), 
#                    'password': forms.PasswordInput(attrs={'class':'form-control'}),}
#

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['codigo','nombre','tipoCurso','valor','imagen']
        labels = {'codigo':'codigo','nombre':'nombre','tipoCurso':'tipo de Curso','valor':'valor','imagen':'imagen'}


class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ['usuario','curso','fecha_matricula', 'activo']
        labels = {'usuario.nombreCompleto:usuario.nombreCompleto','curso.nombre:curso.nombre','fechaMatricula:fechaMatricula','activo:activo'}

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

class CursoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Curso
        fields = ['codigo','nombre','tipoCurso','valor','imagen']


class UsuarioForm(UserCreationForm):

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        ]
        labels = {
                'username': 'nombre de usuario',
                'first_name':'Nombre',
                'last_name': 'Apellido',
                'email': 'Mail',
                'password1': 'Contraseña',
                'password2': 'Repite Contraseña',
        }