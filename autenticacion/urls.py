from django.urls import path
from autenticacion import views


urlpatterns = [
    path('registro/', views.VRegistro.as_view(), name='autenticacion'),
]