from django.shortcuts import render
from .models import Servico
from .models import Agendamento

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


@api_view(['GET', 'POST'])
def listarServico(request):
    if request.method == 'GET':
     servico = Servico.objects.all()
     serializer = ServicoSerializer(servico, many = True)
