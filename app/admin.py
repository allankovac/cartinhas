from django.contrib import admin

# Register your models here.
from .models import Posicao,Time,Atleta,Etapa,Rodada,Nota


admin.site.register(Posicao)
admin.site.register(Time)
admin.site.register(Atleta)
admin.site.register(Etapa)
admin.site.register(Rodada)
admin.site.register(Nota)