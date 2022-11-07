from rolGame.models import juego_rol
from random import randint

class Battleship:
    def __init__(self,vida,fuerza):
        self.vida=vida
        self.fuerza=fuerza

def atack():
    return randint(1,12)
     
player=Battleship(150, 1)
enemy=Battleship(120,1)

atk= atack()
res_atk = enemy.vida/atk

def after_attack(res_atk):
    if res_atk < 40:
        atk1= juego_rol.objects.filter(id=3)
        return atk1



