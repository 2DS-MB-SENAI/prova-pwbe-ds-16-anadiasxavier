from django.contrib import admin
from .models import Servico
from .models import Agendamento


admin.site.register(Servico)
admin.site.register(Agendamento)
