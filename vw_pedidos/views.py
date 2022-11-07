
from django.shortcuts import redirect, render

from .carta import Carro
from virtualWaiter.models import Articulos
from django.views.generic import ListView

# Create your views here.
'''
def carta(request):
    articulo= Articulos.objects.all()
    return render(request, "vw_pedidos/carta.html", {'articulo':articulo})
class cartaList(ListView):
    model = Articulos
    template_name = 'vw_pedidos/carta.html'
    
    def get_queryset(self):
       return super().get_queryset().filter(articulo__categoria='categoria')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context
    
'''

def carta(request):
    entrantes = Articulos.objects.filter(categoria=1)
    ensaladas = Articulos.objects.filter(categoria=2)
    pastas = Articulos.objects.filter(categoria=3)
    pizzas = Articulos.objects.filter(categoria=4)
    postres = Articulos.objects.filter(categoria=5)
    bebidas = Articulos.objects.filter(categoria=6)

    data = {
        'entrantes': entrantes,
        'ensaladas': ensaladas,
        'pastas': pastas,
        'pizzas': pizzas,
        'postres': postres,
        'bebidas': bebidas,
    }
    return render(request, "vw_pedidos/carta.html", data)

def agregar_articulo(request, id_articulo):
    carro=Carro(request)
    articulo=Articulos.objects.get(id=id_articulo)
    carro.agregar(articulo=articulo)
    return redirect('carro:carta')

def elimina_articulo(request, id_articulo):
    carro=Carro(request)
    articulo=Articulos.objects.get(id=id_articulo)
    carro.eliminar_articulo(articulo=articulo)
    return redirect("carta")

def resta_articulo(request, id_articulo):
    carro=Carro(request)
    articulo=Articulos.objects.get(id=id_articulo)
    carro.restar_articulo(articulo=articulo)
    return redirect("carro:carta")

def limpia_pedido(request):
    carro=Carro(request)
    carro.limpiar_pedido
    return redirect("carta")

