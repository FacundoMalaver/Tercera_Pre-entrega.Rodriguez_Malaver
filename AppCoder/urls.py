from django.urls import path
from .views import *

urlpatterns = [
        path('estudiantes', estudiantes, name="estudiantes"),
        path('profesores', profesores, name="profesores"),
        path('cursos', cursos, name="cursos"),
        path('entregables', entregables, name="entregables"),
        path('buscar', buscar, name="buscar"),
        path('sedes', sedes, name="sedes")

]