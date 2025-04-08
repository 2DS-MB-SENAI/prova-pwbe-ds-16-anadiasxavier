from django.db import models
from django.core.validators import MinLengthValidator


class Medico(models.Model):
    nome = models.CharField(max_length=255, validators=[MinLengthValidator(5)])
    especialidade_escolhas = (
     ('PEDIATRIA', 'Pediatria'),
     ('CAR','Car'),
     ('ORTOPEDIA', 'Ortopedia'),
     ('OFTALMOLOGIA','Oftalmologia'),
    )
    especialidade = models.CharField(max_length=15, choices=especialidade_escolhas)
    crm = models.CharField(max_length=255 , null=True, blank=True )
    email = models.EmailField(max_length=255)
    REQUIRED_FIELDS = ['nome', 'especialidade','crm']

def __str__(self):
        return self.nome

class Consulta(models.Model):
    paciente = models.CharField(max_length=255)
    data = models.DateTimeField()
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    status_escolhas =(
        ('AGENDADO', 'Agendado'),
        ('REALIZADO', 'Realizado'),
        ('CANCELADO', 'Cancelado'),
        )
    status = models.CharField(max_length=15, choices=status_escolhas)