
from django.shortcuts import render, redirect
from django.http import HttpRequest

from .forms import categoria, modelo_carta
from .models import Articulos, Iva, Categoria
# Create your views here.


class formulario_articulo_View(HttpRequest):
   
    # formulario para crear artículo
    
    def index(request):
        articulo = modelo_carta()
        return render(request, 'virtualWaiter/anadirArticulo.html', {"form":articulo})

  
    # crear artículo
    
    def proceso_formulario(request,):
        articulo = modelo_carta(request.POST)
        if articulo.is_valid():
            articulo.save()
        articulo = Articulos.objects.all().order_by('categoria')
        return render(request, 'virtualWaiter/listaArticulos.html', {"articulo":articulo, "mensaje_creado":"ok"})

    # pagina de base de datos 

  
    
    def listar_articulos(request):
        articulo = Articulos.objects.all().order_by('categoria')
        return render(request, "virtualWaiter/listaArticulos.html", {"articulo":articulo})

    # formulario editar datos

    def edit(request, id_articulo):
        articulo = Articulos.objects.filter(id=id_articulo).first()
        form = modelo_carta(instance=articulo)
        return render(request, "virtualWaiter/articuloEdit.html", {"form": form, "articulo":articulo})

    # validar datos

    def actualizar_articulo(request, id_articulo):
        articulo = Articulos.objects.get(pk=id_articulo)
        form = modelo_carta(request.POST, instance=articulo)
        if form.is_valid():
            form.save()
        articulo = Articulos.objects.all()
        return render(request, "virtualWaiter/listaArticulos.html", {"articulo":articulo, "mensaje_editado":"ok"})
    
    # borrar artículo 

    def delete_articulo(request, id_articulo):
        articulo = Articulos.objects.get(pk=id_articulo)
        if request.method == "POST":
            articulo.delete()
            return redirect('listaArticulos')
        articulo = Articulos.objects.all()
        return render(request, "virtualWaiter/listaArticulos.html", {"articulo":articulo, "mensaje_borrado":"ok"}) 

   