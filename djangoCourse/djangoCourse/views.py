import json

from django.http import HttpResponse
from django.shortcuts import render


# FUNCTION-based views
def home(request):    
    lista = [
        {'nome': 'Pedro', 'sexo': 'm'},
        {'nome': 'Maria', 'sexo': 'f'},
        {'nome': 'Jose', 'sexo': 'm'},
        {'nome': 'Ana', 'sexo': 'f'}
    ]

    sexo = 'm'
    nome = 'Maria Jose'
    minha_variavel = 'Hello World atraves de variavel'
    return render(request, 'index.html', {'minha_variavel': minha_variavel,
                                          'sexo': sexo,
                                          'nome': nome,
                                          'lista': lista})