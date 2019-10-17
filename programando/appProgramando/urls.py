from django.urls import path, include
from . import views

urlpatterns = [
    
    path('', views.index),
    path('testimonios', views.testimonios),
    path('suscripcion', views.suscripcion),
    #----- usuario -----
    path('agregarUsuario', views.crearUsuario), #create
    path('borrarUsuario/<int:usuarioId>', views.borrarUsuario), #delete
    path('editarUsuario/<int:usuarioId>', views.editarUsuario), #edit
    path('listarUsuariosFull', views.listarUsuarioFull), #readFull
    path('listarUsuarios', views.listarUsuarios), #read
    # ----- Curso ----
    path('agregarCurso', views.crearCurso), #create
    path('borrarCurso/<int:cursoId>', views.borrarCurso), #delete
    path('editarCurso/<int:cursoId>', views.editarCurso), #edit
    path('listarCursosFull', views.listarCursosFull), #readFull
    path('listarCursos', views.listarCursos), #read
   
]