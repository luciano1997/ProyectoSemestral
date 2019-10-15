from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from django.urls import reverse_lazy
# Create your views here.
from .models import Usuario, Curso, Alumno
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

# todo lo nuevo CRUD

def crearUsuario(request):
    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect('/agregarUsuario')
    else:
        form = UsuarioForm()
        return render(request, 'appProgramando/agregarUsuario.html',
                      {'form': form})

def listarUsuarios(request):
    # creamos una coleccion la cual carga todos los registros
    usuario = Usuario.objects.all()
    # renderizamos la coleccion en el template
    return render(request,
                "appProgramando/listarUsuarios.html", {'usuarios': usuario}) 
def listarUsuarioFull(request):
    #creamos una coleccion la cual carga todos los registros
    usuario = Usuario.objects.all()
    #renderizamos la coleccion en el template
    return render(request, 
            "appProgramando/listarUsuariosFull.html", {'usuarios': usuario})


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
    return render(request, "appProgramando/editarUsuario.html", {'form':form})   


def borrarUsuario(request, usuarioId):
    instacia = Usuario.objects.get(id=usuarioId)
    instacia.delete()
    return redirect('/')

 

#class agregarUsuario(CreateView):  #Carrera_Create
#    model = Usuario
#    form_class = UsuarioForm
#    templates_name = 'appProgramando/inscripcion_carrera.html'
#    success_url = reverse_lazy('carrera_crear')

def editar_carrera(request, carrera_id):
    instancia= Carrera.objects.get(id=carrera_id)
    form= CarreraForm(instance=instancia)
    if request.method=="POST":
        #Actualizamos el Formulario con los datos del objeto
        form=CarreraForm(request.POST, instance=instancia)
        #si el formulario es valido...
        if form.is_valid():
            #guardamos el formulario pero sin confirmar aun
            instancia= form.save(commit=False)
            #grabamos!!
            instancia.save()
    return render(request,"app/editar_carrera.html",{'form':form})

def borrar_carrera(request, carrera_id):
    instacia= Carrera.objects.get(id=carrera_id)
    instacia.delete()
    return redirect('/')


