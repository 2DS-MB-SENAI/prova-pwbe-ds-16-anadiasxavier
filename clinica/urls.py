from django.urls import path
from . import views

urlpatterns = [
    path('medicos/', views.listar_medicos, name='listar_medicos'),
    path('consultas/nova/', views.criar_consulta, name='nova_consulta'),
    path('consultas/<int:pk>/', views. detalhes_consulta, name = 'listar_consultas'),
]