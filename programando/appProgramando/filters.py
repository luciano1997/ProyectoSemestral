from .models import Curso, Alumno
import django_filters

class CursoFilter(django_filters.FilterSet):
    class Meta:
        model = Curso
        fields = ['tipoCurso',]
        labels = {'tipoCurso': 'Tipo de Curso'}
        

class AlumnoFilter(django_filters.FilterSet):
    class Meta:
        model = Alumno
        fields = ['activo',]
        labels = {'activo': 'activo'}
                