from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.

def estudiantes(request):
    if request.method=="POST":
        form=EstudiantesForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombre=info["nombre"]
            appelido=info["apellido"]
            email=info["email"]
            estudiantes=Estudiante(nombre=nombre,apellido=appelido,email=email)
            estudiantes.save()
            mensaje="Estudiante guardado"
        else:
            mensaje="Datos invalidos"
        estudiantes=Estudiante.objects.all()
        formulario_estudiantes=EstudiantesForm()
        return render(request, "AppCoder/estudiantes.html", {"mensaje":mensaje, "formulario":formulario_estudiantes, "estudiantes":estudiantes})
    else:
        estudiantes=Estudiante.objects.all()
        formulario_estudiantes=EstudiantesForm()
    return render(request, "AppCoder/estudiantes.html", {"formulario":formulario_estudiantes, "estudiantes":estudiantes})

def entregables(request):
    if request.method=="POST":
        form=EntregablesForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombre=info["nombre"]
            fecha=info["fecha"]
            entregado=info["entregado"]
            entregables=Entregables(nombre=nombre,entregado=entregado,fecha=fecha)
            entregables.save()
            mensaje="Entrega guardada"
        else:
            mensaje="Datos invalidos"
        entregables=Entregables.objects.all()
        formulario_entregables=EntregablesForm()
        return render(request, "AppCoder/entregables.html", {"mensaje":mensaje, "formulario":formulario_entregables, "entregables":entregables})
    else:
        entregables=Entregables.objects.all()
        formulario_entregables=EntregablesForm()
    return render(request, "AppCoder/entregables.html", {"formulario":formulario_entregables, "entregables":entregables})

def cursos(request):
    if request.method=="POST":
        form=CursoForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombre=info["nombre"]
            comision=info["comision"]
            curso=Curso(nombre=nombre,comision=comision)
            curso.save()
            mensaje="Curso creado"
        else:
            mensaje="Datos invalidos"
        cursos=Curso.objects.all()
        formulario_curso=CursoForm()
        return render(request, "AppCoder/cursos.html", {"mensaje":mensaje, "formulario":formulario_curso, "cursos":cursos})
    else:
        cursos=Curso.objects.all()
        formulario_curso=CursoForm()
        return render(request, "AppCoder/cursos.html", {"formulario":formulario_curso, "cursos":cursos})
    
def profesores(request):
    if request.method=="POST":
        form=ProfesForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombre=info["nombre"]
            appelido=info["apellido"]
            email=info["email"]
            profesion=info["profesion"]
            profesores=Profesor(nombre=nombre,apellido=appelido,email=email,profesion=profesion)
            profesores.save()
            mensaje="Profesor guardado"
        else:
            mensaje="Datos invalidos"
        profesores=Profesor.objects.all()
        formulario_profesores=ProfesForm()
        return render(request, "AppCoder/profesores.html", {"mensaje":mensaje, "formularioProfes":formulario_profesores, "profesores":profesores})
    else:
        formulario_profesores=ProfesForm()
        profesores=Profesor.objects.all()
    return render(request, "AppCoder/profesores.html", {"formularioProfes":formulario_profesores, "profesores":profesores})
    
def inicio(request):
    return render(request, "AppCoder/inicio.html")

def buscar(request):
    comision=request.GET['comision']
    if comision!="":
        cursos=Curso.objects.filter(comision__icontains=comision)
        return render(request, "AppCoder/resultadosBusqueda.html", {"cursos":cursos})
    else:
        return render(request, "AppCoder/inicio.html", {"mensaje":"Ingrese una comision"})
    
def sedes(request):
    if request.method=="POST":
        form=SedesForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombre=info["nombre"]
            direccion=info["direccion"]
            telefono=info["telefono"]
            sedes=Sedes(nombre=nombre,direccion=direccion,telefono=telefono)
            sedes.save()
            mensaje="Sede guardada"
        else:
            mensaje="Datos invalidos"
        sedes=Sedes.objects.all()
        formulario_sedes=SedesForm()
        return render(request, "AppCoder/sedes.html", {"mensaje":mensaje, "formulario":formulario_sedes, "sedes":sedes})
    else:
        sedes=Sedes.objects.all()
        formulario_sedes=SedesForm()
    return render(request, "AppCoder/sedes.html", {"formulario":formulario_sedes, "sedes":sedes})