from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def clientes(request):
    return HttpResponse(json.dumps({'clientes': ['Maria', 'José', 'João']}))

def cliente_detalhe(request, id):
    return HttpResponse(f'cliente_detalhe: {id}')

def cliente_por_nome(request, nome):
    return HttpResponse('Ola %s' % nome)