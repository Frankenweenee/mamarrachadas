from django.urls import path
from rolGame import views


urlpatterns = [
    path('start/', views.start, name='start'),
    path('game/', views.game, name='game'),
    path('game1/', views.game_fly, name='fly'),
]