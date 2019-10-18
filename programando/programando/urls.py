"""programando URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('appProgramando.urls')),
    path('testimonios', include('appProgramando.urls')),
    path('suscripcion', include('appProgramando.urls')),
    # ---- Usuarios ----
    path('listarUsuarios', include('appProgramando.urls')),
    path('editarUsuario/<int:usuarioId>', include('appProgramando.urls')),
    path('borrarUsuario/<int:usuarioId>', include('appProgramando.urls')),
    path('agregarUsuario', include('appProgramando.urls')),
    path('listarUsuariosFull', include('appProgramando.urls')),
    # ---- CURSOS ------
    path('agregarCurso',include('appProgramando.urls')), #create
    path('borrarCurso/<int:cursoId>',include('appProgramando.urls')), #delete
    path('editarCurso/<int:cursoId>',include('appProgramando.urls')), #edit
    path('listarCursosFull', include('appProgramando.urls')), #readFull
    path('listarCursos', include('appProgramando.urls')), #read
    # ---- Alumnos ----
    path('agregarAlumno',include('appProgramando.urls')), #create
    path('borrarAlumno/<int:alumnoId>',include('appProgramando.urls')), #delete
    path('editarAlumno/<int:alumnoId>',include('appProgramando.urls')), #edit
    path('listarAlumnosFull', include('appProgramando.urls')), #readFull
    path('listarAlumnos', include('appProgramando.urls')), #read
]
