from django.shortcuts import render

# Create your views here.
from .models import Curso, Alumno, Usuario
#from mantenedor.app.forms import CarreraForm
from .forms import UsuarioForm

def usuarios_list(request):
    return render(request, 'appProgramando/usuarios_list.html', {})

def index(request):
    return render(request, 'appProgramando/index.html', {})

def testimonios(request):
    return (render(request, 'appProgramando/testimonios.html', {}))

def suscripcion(request): 
    return render(request, 'appProgramando/suscripcion.html', {})

def listar_usuarios_full(request):
    #creamos una coleccion la cual carga todos los registros
    usuario = Usuario.objects.all()
    #renderizamos la coleccion en el template
    return render(request, 
            "appProgramando/usuarios_list.html", {'usuarios': usuario})
