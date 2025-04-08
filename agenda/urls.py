from django.urls import path
from . import views

urlpatterns = [
    path('api/servicos/', views.listarServico),
    path('api/servicos/<int:pk>', views.servicoDetalhes),
    path('api/agendamentos/', views.listarAgendamento),
     path('api/agendamentos/<int:pk>', views.agendamentoDetalhes),
]