from django.contrib import admin
from .models import Consulta
from .models import Medico

class ConsultaAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'medico', 'data', 'status')
    search_fields = ('paciente', 'nome')


class MedicoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'especialidade')  
    search_fields = ('nome',)

# Register your models here.
admin.site.register(Consulta, ConsultaAdmin)
admin.site.register(Medico, MedicoAdmin)