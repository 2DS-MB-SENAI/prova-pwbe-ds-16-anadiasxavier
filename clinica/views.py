from django.shortcuts import render, redirect, get_object_or_404

from .models import Medico
from .models import Consulta
from .forms import ConsultaForm


def listar_medicos(request):
    medicos = Medico.objects.all()
    return render(request, 'clinica/listar_medicos.html', {'medicos': medicos})

def criar_consulta(request):
    if request.method == 'POST':
        form = ConsultaForm(request.POST)
        if form.is_valid():
             form.save()
             return redirect('listar_medicos')
    else:
        form = ConsultaForm()
    return render(request, 'clinica/form_consulta.html', {'form': form})

def detalhes_consulta(request, pk):
        consulta = get_object_or_404(Consulta, pk=pk)
        return render(request, 'clinica/listar_consultas.html', {'consulta': consulta})
           
