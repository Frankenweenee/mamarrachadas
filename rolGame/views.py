from django.shortcuts import render
from .models import juego_rol, nameDb
from .beast_attack import *


# Create your views here.

def start(request):
    return render(request, 'rolGame/start.html')

def game(request):
    mision = juego_rol.objects.filter(id=1)
    nameFi = nameDb
    return render(request, 'rolGame/game.html', {"misiones":mision, "name":nameFi})


def game_fly(request):
    mision2 = juego_rol.objects.filter(id=2)
    
    return render (request, 'rolGame/game.html',{"misiones2":mision2})
#print(name)
def first_shot(request):
    mision3 = after_attack(res_atk)
    return render (request, 'rolGame/game.html',{"misiones3":mision3})