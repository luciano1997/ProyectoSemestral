from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
# Create your views here.
from .models import Curso, Alumno #Usuario,
#from .models import Usuario, Curso, Alumno

from appProgramando.forms import UsuarioForm, CursoForm, AlumnoForm

from .filters import CursoFilter, AlumnoFilter


def usuarios_list(request):
    return render(request, 'appProgramando/usuarios_list.html', {})


def index(request):
    return render(request, 'appProgramando/index.html', {})


def testimonios(request):
    return (render(request, 'appProgramando/testimonios.html', {}))


def suscripcion(request):
    return render(request, 'appProgramando/suscripcion.html', {})

# todo lo nuevo CRUD
# --- USUARIO ---

class RegistroUsuario(CreateView):
    model = User
    template_name = "appProgramando/usuarioCrud/agregarUsuario.html"
    form_class = UsuarioForm
    success_url = reverse_lazy('index')


def listarUsuarios(request):
    # creamos una coleccion la cual carga todos los registros
    usuario = User.objects.all()
    # renderizamos la coleccion en el template
    return render(request,
                "appProgramando/usuarioCrud/listarUsuarios.html", {'usuarios': usuario}) 

@login_required
def listarUsuarioFull(request):
    #creamos una coleccion la cual carga todos los registros
    usuario = User.objects.all()
    #renderizamos la coleccion en el template
    return render(request, 
            "appProgramando/usuarioCrud/listarUsuariosFull.html", {'usuarios': usuario})


def editarUsuario(request, usuarioId):
    instancia= Usuario.objects.get(id=usuarioId)
    form= UsuarioForm(instance=instancia)
    if request.method=="POST":
        #Actualizamos el Formulario con los datos del objeto
        form=UsuarioForm(request.POST, instance=instancia)
        #si el form es valido
        if form.is_valid():
            #guardamos el formulario pero sin confirmar aun
            instancia= form.save(commit=False)
            #grabamos
            instancia.save()
    return render(request, "appProgramando/usuarioCrud/editarUsuario.html", {'form':form})   


def borrarUsuario(request, usuarioId):
    instacia = User.objects.get(id=usuarioId)
    instacia.delete()
    return redirect('/')

#--- CURSOS ---
 
class CreateCurso(CreateView): # new
    model = Curso
    form_class = CursoForm
    template_name = "appProgramando/usuarioCrud/agregarUsuario.html"
    success_url = reverse_lazy('index')


def listarCursos(request):
    # creamos una coleccion la cual carga todos los registros
    curso = Curso.objects.all().filter(tipoCurso='Desarrollo Web')
    # renderizamos la coleccion en el template
    return render(request,
            "appProgramando/cursoCrud/listarCursos.html", {'cursos': curso}) 
            
@login_required
def listarCursosFull(request):
    #creamos una coleccion la cual carga todos los registros
    curso = Curso.objects.all()
    #renderizamos la coleccion en el template
    return render(request, 
            "appProgramando/cursoCrud/listarCursosFull.html", {'cursos': curso})

@login_required
def editarCurso(request, cursoId):
    instancia= Curso.objects.get(id=cursoId)
    form= CursoForm(instance=instancia)
    if request.method=="POST":
        #Actualizamos el Formulario con los datos del objeto
        form=CursoForm(request.POST, instance=instancia)
        #si el form es valido
        if form.is_valid():
            #guardamos el formulario pero sin confirmar aun
            instancia= form.save(commit=False)
            #grabamos
            instancia.save()
    return render(request, "appProgramando/cursoCrud/editarCurso.html", {'form':form})   

@login_required
def borrarCurso(request, cursoId):
    instacia = Curso.objects.get(id=cursoId)
    instacia.delete()
    return redirect('/')


# --- ALUMNOS ----



class RegistroAlumno(CreateView):
    model = Alumno
    template_name = "appProgramando/alumnoCrud/agregarAlumno.html"
    form_class = AlumnoForm
    success_url = reverse_lazy("index")

@login_required
def listarAlumnos(request):
    # creamos una coleccion la cual carga todos los registros
    alumno = Alumno.objects.all()
    # renderizamos la coleccion en el template

    return render(request,
                "appProgramando/alumnoCrud/listarAlumnos.html", {'alumnos': alumno}) 

@login_required
def listarAlumnosFull(request):
    #creamos una coleccion la cual carga todos los registros
    alumno = Alumno.objects.all()
    #renderizamos la coleccion en el template
    return render(request, 
            "appProgramando/alumnoCrud/listarAlumnosFull.html", {'alumnos': alumno})

@login_required
def editarAlumno(request, alumnoId):
    instancia= Alumno.objects.get(id=alumnoId)
    form= AlumnoForm(instance=instancia)
    if request.method=="POST":
        #Actualizamos el Formulario con los datos del objeto
        form=AlumnoForm(request.POST, instance=instancia)
        #si el form es valido
        if form.is_valid():
            #guardamos el formulario pero sin confirmar aun
            instancia= form.save(commit=False)
            #grabamos
            instancia.save()
    return render(request, "appProgramando/alumnoCrud/editarAlumno.html", {'form':form})   

@login_required
def borrarAlumno(request, alumnoId):
    instacia = Alumno.objects.get(id=alumnoId)
    instacia.delete()
    return redirect('/')




#### django filter


def search(request):
    curso_list = Curso.objects.all()
    curso_filter = CursoFilter(request.GET, queryset=curso_list)
    return render(request, 'appProgramando/cursoCrud/listarCursos.html', {'filter': curso_filter})

def searchAlumno(request):
    alumno_list = Alumno.objects.all()
    alumno_filter = AlumnoFilter(request.GET, queryset=alumno_list)
    return render(request, 'appProgramando/alumnoCrud/listarAlumnos.html', {'filter': alumno_filter})    



