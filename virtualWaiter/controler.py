
from .models import Categoria, Iva, Articulos
from .forms import modelo_carta, iva, categoria



    
def agregar_iva(self, request):
    agre_iva = iva(request.POST)
    if agre_iva.is_valid():
        agre_iva.save()


def proceso_formu(request):
        articulo = modelo_carta(request.POST)
        if articulo.is_valid():
            articulo.save()