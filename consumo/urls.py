from django.urls import path
from consumo import views


urlpatterns = [
    path('', views.consumo, name='consumo'),
    path('', views.buscar, name='extra'),
]