from django.shortcuts import render
from django.http import HttpResponse
import json 
# Create your views here.
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view

@api_view(['GET']) # Preciso adicionar esse decorator para que a minha rota aceite o decorator permission_classes
@permission_classes([IsAuthenticated]) # preciso desse decorator para que minha rota requira autenticacao
def clientes(request):
    return HttpResponse(json.dumps({'clientes': ['Maria', 'José', 'João']}))

@permission_classes([IsAuthenticated])
def cliente_detalhe(request, id):
    return HttpResponse(f'cliente_detalhe: {id}')

@permission_classes([IsAuthenticated])
def cliente_por_nome(request, nome):
    return HttpResponse('Ola %s' % nome)