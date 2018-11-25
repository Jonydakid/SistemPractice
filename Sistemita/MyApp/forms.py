#Siempre se importa el forms y con ello las clases de los modelos
from django import forms
from .models import Persona,Cancion

class addUser(forms.Form):
    first_name=forms.CharField(widget=forms.TextInput(),label="Ingrese su Nombre")
    last_name=forms.CharField(widget=forms.TextInput(),label="Ingrese su Apellido")
    username=forms.CharField(widget=forms.TextInput(),label="Ingreso Nombre Usuario")
    password=forms.CharField(widget=forms.PasswordInput(),label="Ingreso de Contraseña")
    email=forms.EmailField(widget=forms.EmailInput(),label="Email")

class addSong(forms.Form):
    song=forms.FileField(widget=forms.FileInput(),label='Ingrese canción')
