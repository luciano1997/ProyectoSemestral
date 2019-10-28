from .models import Curso
import django_filters

class CursoFilter(django_filters.FilterSet):
    class Meta:
        model = Curso
        fields = ['tipoCurso',]
        labels = {'tipoCurso': 'Tipo de Curso'}
        