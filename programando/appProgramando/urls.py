from django.urls import path, include
from . import views
from .views import RegistroUsuario
urlpatterns = [
    
    path('', views.index, name='index',),
    path('testimonios', views.testimonios),
    path('suscripcion', views.suscripcion),
    #----- usuario -----
    path('agregarUsuario', views.RegistroUsuario.as_view()), #create
    path('borrarUsuario/<int:usuarioId>', views.borrarUsuario), #delete
    path('editarUsuario/<int:usuarioId>', views.editarUsuario), #edit
    path('listarUsuariosFull', views.listarUsuarioFull), #readFull
    path('listarUsuarios', views.listarUsuarios), #read
    # ----- Curso ----
    path('agregarCurso', views.CreateCurso.as_view()), #create
    path('borrarCurso/<int:cursoId>', views.borrarCurso), #delete
    path('editarCurso/<int:cursoId>', views.editarCurso), #edit
    path('listarCursosFull', views.listarCursosFull), #readFull
    path('listarCursos', views.search, name='search'), #read

    #path('cursosList', views.cursosList), #read

    # ---- Alumno ---- 
    path('agregarAlumno', views.RegistroAlumno.as_view()), #create
    path('borrarAlumno/<int:alumnoId>', views.borrarAlumno), #delete
    path('editarAlumno/<int:alumnoId>', views.editarAlumno), #edit
    path('listarAlumnosFull', views.listarAlumnosFull), #readFull
    path('listarAlumnos', views.searchAlumno, name='searchAlumno'), #read

    
    
]