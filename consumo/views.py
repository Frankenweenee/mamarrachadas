
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def consumo(request):
    return render(request,'consumo/consumo.html')

def buscar(request):
    return render(request, 'consumo/extra.html')
