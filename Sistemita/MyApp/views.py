from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import Cancion, Persona
from .forms import addSong, addUser
from django.template import loader
import os

"""@login_required(login_url='ingresar')
def registrar_mascota(request):
    form=RegistrarMascota(request.POST,request.FILES or None)
    if form.is_valid():
        data=form.cleaned_data
        masc=Mascota(fotoMascota=request.FILES['fotoMascota'],nombreMascota=data.get("nombreMascota"),raza=data.get("raza"),descripcion=data.get("descripcion"),estado=data.get("estado"))
        a=False
        b=1
        while a!=True:
                if Mascota.objects.filter(codigoMascota=b).count()<=0:
                    masc.codigoMascota=b
                    masc.save()
                    a=True
                b=b+1
        return redirect('gestion')
    form=RegistrarMascota()
    return render(request,'reg_mascota.html',{'form':form,})"""
# Create your views here.
def index(request):
    
    form=addSong(request.POST or None)
    
    return render(request,'index.html',{'form':form,})

def registro(request):
    return render(request,'registro.html')
"""
A invitados, mostrará canciones disponibles en el servidor (de muestra, no de otros usuarios)
a usuarios, se les permitirá agregar canciones al servidor y quedaría guardado como su playlist,
además tendrá un buscador para otros usuarios con sus respectivos playlist
"""
def canciones(request):
    return render(request,'canciones.html')

def salir(request):
    logout(request)
    return redirect("/")
    


"""@require_POST
def file_upload(request):
    save_path = os.path.join(settings.MEDIA_ROOT, 'uploads', request.FILES['file'])
    path = Cancion.save(save_path, request.FILES['file'])
    document = Cancion.objects.create(document=path, upload_by=request.user)
    return JsonResponse({'document': document.id})
"""