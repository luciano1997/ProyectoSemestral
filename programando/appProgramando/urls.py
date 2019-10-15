from django.urls import path, include
from . import views

urlpatterns = [
    path('listarUsuarios', views.listarUsuarios),
    path('', views.index),
    path('testimonios', views.testimonios),
    path('suscripcion', views.suscripcion),
    path('borrarUsuario/<int:usuarioId>', views.borrarUsuario),
    path('editarUsuario/<int:usuarioId>', views.editarUsuario),
    path('agregarUsuario', views.crearUsuario),
    path('listarUsuariosFull', views.listarUsuarioFull),
   
]