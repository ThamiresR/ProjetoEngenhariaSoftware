from django.contrib import admin
from .models import Computador, Coordenador, Aluno, Projeto, Reserva
# Register your models here.

admin.site.register(Computador)
admin.site.register(Coordenador)
admin.site.register(Aluno)
admin.site.register(Projeto)
admin.site.register(Reserva)