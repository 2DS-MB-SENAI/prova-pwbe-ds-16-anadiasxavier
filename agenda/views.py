from django.shortcuts import render
from .models import Servico
from .models import Agendamento
from .serializers import ServicoSerializer
from .serializers import AgendamentoSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


@api_view(['GET', 'POST'])
def listarServico(request):
    if request.method == 'GET':
     servico = Servico.objects.all()
     serializer = ServicoSerializer(servico, many = True)
     return Response(serializer.data)
    elif request.method == 'POST':
     serializer = ServicoSerializer(data=request.data, many=isinstance(request.data, list))
     if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

@api_view(['GET'])
def servicoDetalhes(request, pk):
    try:
        servico = Servico.objects.get(pk=pk)
    except servico.DoesNotExist: 
        return Response({'erro': 'Servico inexistente'}, status=status.HTTP_404_NOT_FOUND)

    serializer = ServicoSerializer(servico)
    return Response(serializer.data)
  
@api_view(['GET', 'POST'])
def listarAgendamento(request):
    if request.method == 'GET':
     agendamento = Agendamento.objects.all()
     serializer = AgendamentoSerializer(agendamento, many = True)
     return Response(serializer.data)
    elif request.method == 'POST':
     serializer = AgendamentoSerializer(data=request.data, many=isinstance(request.data, list))
     if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

@api_view(['GET'])
def agendamentoDetalhes(request, pk):
    try:
        agendamento = Agendamento.objects.get(pk=pk)
    except Agendamento.DoesNotExist: 
        return Response({'erro': 'Agendamento inexistente'}, status=status.HTTP_404_NOT_FOUND)

    serializer = AgendamentoSerializer(agendamento)
    return Response(serializer.data)