from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from django.urls import reverse_lazy
# Create your views here.
from appProgramando.models import Usuario,Curso,Alumno
#from .models import Usuario, Curso, Alumno

from appProgramando.forms import UsuarioForm, CursoForm, AlumnoForm

from .filters import CursoFilter


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
def crearUsuario(request):
    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect('/agregarUsuario')
    else:
        form = UsuarioForm()
        return render(request, 'appProgramando/usuarioCrud/agregarUsuario.html',
                      {'form': form})

def listarUsuarios(request):
    # creamos una coleccion la cual carga todos los registros
    usuario = Usuario.objects.all()
    # renderizamos la coleccion en el template
    return render(request,
                "appProgramando/usuarioCrud/listarUsuarios.html", {'usuarios': usuario}) 

def listarUsuarioFull(request):
    #creamos una coleccion la cual carga todos los registros
    usuario = Usuario.objects.all()
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
    instacia = Usuario.objects.get(id=usuarioId)
    instacia.delete()
    return redirect('/')

#--- CURSOS ---
 
def crearCurso(request):
    if request.method == "POST":
        form = CursoForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect('/agregarCurso')
    else:
        form = CursoForm()
        return render(request, 'appProgramando/cursoCrud/agregarCurso.html',
                      {'form': form})

def listarCursos(request):
    # creamos una coleccion la cual carga todos los registros
    curso = Curso.objects.all().filter(tipoCurso='Desarrollo Web')
    # renderizamos la coleccion en el template
    return render(request,
            "appProgramando/cursoCrud/listarCursos.html", {'cursos': curso}) 

def listarCursosFull(request):
    #creamos una coleccion la cual carga todos los registros
    curso = Curso.objects.all()
    #renderizamos la coleccion en el template
    return render(request, 
            "appProgramando/cursoCrud/listarCursosFull.html", {'cursos': curso})


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


def borrarCurso(request, cursoId):
    instacia = Curso.objects.get(id=cursoId)
    instacia.delete()
    return redirect('/')


# --- ALUMNOS ----

def crearAlumno(request):
    if request.method == "POST":
        form = AlumnoForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect('/agregarAlumno')
    else:
        form = AlumnoForm()
        return render(request, 'appProgramando/alumnoCrud/agregarAlumno.html',
                      {'form': form})

def listarAlumnos(request):
    # creamos una coleccion la cual carga todos los registros
    alumno = Alumno.objects.all()
    # renderizamos la coleccion en el template

    return render(request,
                "appProgramando/alumnoCrud/listarAlumnos.html", {'alumnos': alumno}) 

def listarAlumnosFull(request):
    #creamos una coleccion la cual carga todos los registros
    alumno = Alumno.objects.all()
    #renderizamos la coleccion en el template
    return render(request, 
            "appProgramando/alumnoCrud/listarAlumnosFull.html", {'alumnos': alumno})


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


def borrarAlumno(request, alumnoId):
    instacia = Alumno.objects.get(id=alumnoId)
    instacia.delete()
    return redirect('/')


def listarCursosProgramacion(request):
    # creamos una coleccion la cual carga todos los registros
    curso = Curso.objects.all().filter(tipoCurso='Programacion')
    # renderizamos la coleccion en el template
    return render(request,
            "appProgramando/cursoCrud/listarCursos.html", {'cursos': curso}) 

    

def listarCursosDesarrolloWeb(request):
    # creamos una coleccion la cual carga todos los registros
    curso = Curso.objects.all().filter(tipoCurso='Desarrollo Web')
    # renderizamos la coleccion en el template
    return render(request,
            "appProgramando/cursoCrud/listarCursos.html", {'cursos': curso}) 





#### django filter


def search(request):
    curso_list = Curso.objects.all()
    curso_filter = CursoFilter(request.GET, queryset=curso_list)
    return render(request, 'appProgramando/cursoCrud/listarCursos.html', {'filter': curso_filter})