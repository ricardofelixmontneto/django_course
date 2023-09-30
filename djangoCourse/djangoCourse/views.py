from django.http import HttpResponse
import json

# FUNCTION-based views
def home(request):
    return HttpResponse('Hello world!')

def clientes(request):
    return HttpResponse(json.dumps({'clientes': ['Maria', 'José', 'João']}))

def cliente_detalhe(request, id):
    return HttpResponse(f'cliente_detalhe: {id}')

def cliente_por_nome(request, nome):
    return HttpResponse('Ola %s' % nome)