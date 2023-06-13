from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from Kayakeando.forms import *

# Create your views here.
def inicio(request):
    return render(request, "Kayakeando/inicio.html")

def kayakistas(request):
        
    kayakistas = Kayakista.objects.all()
    
    return render(request, "Kayakeando/kayakistas.html", {"kayakistas" : kayakistas})


def clubes(request):
    
    clubes = Club.objects.all()
    
    return render(request, "Kayakeando/clubes.html", {"clubes": clubes})


def travesias(request):
    
    travesias = Travesia.objects.all()
    
    return render(request, "Kayakeando/travesias.html", {"travesias":  travesias})


def crearKayakista(request):
    if request.method == "POST":
        miFormulario = KayakistaFormulario(request.POST)
        
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            kayakista = Kayakista(nombre=informacion["nombre"], email=informacion["email"], ubicacion=informacion["ubicacion"], club=informacion["club"])
            kayakista.save()
            miFormulario = Kayakista.objects.all()
            
            return render(request, "Kayakeando/kayakistas.html", {"miFormulario": miFormulario})
        return render(request, "Kayakeando/kayakistas.html", {"miFormulario": miFormulario})
    else:
        miFormulario = KayakistaFormulario()
        
        return render(request, "Kayakeando/formulario_kayakistas.html", {"miFormulario": miFormulario})



def crearClub(request):
    if request.method == "POST":
        miFormulario = ClubFormulario(request.POST)
        
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            club = Club(nombre=informacion["nombre"], email=informacion["email"], localidad=informacion["localidad"], provincia=informacion["provincia"], pais=informacion["pais"])
            club.save()
            
            return render(request, "Kayakeando/clubes.html", {"miFormulario": miFormulario})
    else:
        miFormulario = ClubFormulario()
        
    return render(request, "Kayakeando/formulario_clubes.html", {"miFormulario": miFormulario})


def crearTravesia(request):
    if request.method == "POST":
        miFormulario = TravesiaFormulario(request.POST)
        
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            travesia = Travesia(kayakista=informacion["kayakista"], email=informacion["email"], partida=informacion["partida"], distancia=informacion["distancia"], fecha=informacion["fecha"])
            travesia.save()
            
            return render(request, "Kayakeando/travesias.html", {"miFormulario": miFormulario})
    else:
        miFormulario = TravesiaFormulario()
        
    return render(request, "Kayakeando/formulario_travesias.html", {"miFormulario": miFormulario})



def buscarKayakista(request):
    
    return render(request, "Kayakeando/busqueda.html")


def buscar(request):
    if request.method == "GET":
        miFormulario = BuscarDatoForm(request.GET)
        
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            kayakistas = Kayakista.objects.filter(nombre__icontains = informacion["nombre"])
            
            if kayakistas:
                return render(request, 'Kayakeando/busqueda.html',{"kayakistas": kayakistas})
            else:
                respuesta = "No se encontraron resultados"
                return render(request, "Kayakeando/busqueda.html", {"respuesta":respuesta})
    else:
        miFormulario = BuscarDatoForm()
        return render(request, "Kayakeando/busqueda.html")


