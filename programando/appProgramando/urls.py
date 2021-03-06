from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers, serializers, viewsets
from .views import UserViewSet, UserSerializer, CursoSerializer, CursosViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('cursos', CursosViewSet)
urlpatterns = [
    # api rest
    path('API', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'), name="rest_framework"),


    path('', views.index, name='index'),
    #path('index', views.index, name='index'),
    
    path('testimonios', views.testimonios),
    path('suscripcion', views.suscripcion),
    #----- usuario -----
    path('agregarUsuario', views.RegistroUsuario.as_view()), #create
    path('borrarUsuario/<int:usuarioId>', views.borrarUsuario), #delete
    path('editarUsuario/<int:usuarioId>', views.editarUsuario), #edit
    path('listarUsuariosFull', views.listarUsuarioFull, name="listarUsuariosFull"), #readFull
    path('listarUsuarios', views.listarUsuarios, name='listarUsuarios'), #read
    
    # ----- Curso ----
    path('agregarCurso', views.CreateCurso.as_view()), #create
    path('borrarCurso/<int:cursoId>', views.borrarCurso), #delete
    path('editarCurso/<int:cursoId>', views.editarCurso), #edit
    path('listarCursosFull', views.listarCursosFull, name="listarCursosFull"), #readFull
    path('listarCursos', views.search, name='search'), #read

    #path('cursosList', views.cursosList), #read

    # ---- Alumno ---- 
    path('agregarAlumno', views.RegistroAlumno.as_view(), name='agregarAlumno'), #create
    path('borrarAlumno/<int:alumnoId>', views.borrarAlumno), #delete
    path('editarAlumno/<int:alumnoId>', views.editarAlumno), #edit
    path('listarAlumnosFull', views.listarAlumnosFull, name="listarAlumnosFull"), #readFull
    path('listarAlumnosFilter', views.listarAlumnos, name='listarAlumnosFilter'), #read
    path('listarAlumnos', views.searchAlumno, name='searchAlumno'), #read

    
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)