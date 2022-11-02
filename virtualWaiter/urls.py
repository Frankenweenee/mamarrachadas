from django.urls import path

from virtualWaiter.views import formulario_articulo_View


urlpatterns = [
    path('formulario/', formulario_articulo_View.index, name='form'),
    path('proceso/', formulario_articulo_View.proceso_formulario, name='guardarArticulo'),
    path('lista/', formulario_articulo_View.listar_articulos, name='listaArticulos'),
    path('edit/<int:id_articulo>', formulario_articulo_View.edit, name='articuloEdit'),
    path('actualizar/<int:id_articulo>', formulario_articulo_View.actualizar_articulo, name='articuloActualizado'),
    path('delete/<int:id_articulo>', formulario_articulo_View.delete_articulo, name='delete'),
    
]