from django.urls import path
from web import views



urlpatterns = [
    path('inicio/', views.inicio, name='inicio'),

]