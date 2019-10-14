from django.urls import path, include
from . import views

urlpatterns = [
    path('usuarios', views.usuarios_list),
    path('', views.index),
    path('testimonios', views.testimonios),
    path('suscripcion', views.suscripcion),
   
]