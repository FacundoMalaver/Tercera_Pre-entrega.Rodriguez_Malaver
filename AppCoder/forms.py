from django import forms

class CursoForm(forms.Form):
    nombre=forms.CharField(max_length=50)
    comision=forms.IntegerField()

class ProfesForm(forms.Form):
    nombre=forms.CharField(max_length=50)
    apellido=forms.CharField(max_length=50)
    email=forms.EmailField()
    profesion=forms.CharField(max_length=50)

class EstudiantesForm(forms.Form):
    nombre=forms.CharField(max_length=50)
    apellido=forms.CharField(max_length=50)
    email=forms.EmailField()

class EntregablesForm(forms.Form):
    nombre=forms.CharField(max_length=50)
    fecha=forms.DateField(help_text="eg.:'2006-10-25', '10/25/2006' o '10/25/06'")
    entregado=forms.BooleanField()

class SedesForm(forms.Form):
    nombre=forms.CharField(max_length=50)
    direccion=forms.CharField(max_length=50)
    telefono=forms.IntegerField()
