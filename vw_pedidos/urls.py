from django.urls import path
from vw_pedidos import views

app_name="carro"

urlpatterns = [
    path('carta/', views.carta, name='carta'),
    path('agregar/<int:id_articulo>', views.agregar_articulo, name='agregar'),
    path('eliminar/<int:id_articulo>', views.elimina_articulo, name='eliminar'),
    path('restar/<int:id_articulo>', views.resta_articulo, name='restar'),
    path('limpiar/', views.limpia_pedido, name='limpia'),
    
]