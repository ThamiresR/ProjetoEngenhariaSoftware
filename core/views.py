from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ComputadorSerializer, CoordenadorSerializer, AlunoSerializer, ProjetoSerializer, ReservaSerializer
from .models import Computador, Coordenador, Aluno, Projeto, Reserva
# Create your views here.


class ComputadorViewSet(viewsets.ModelViewSet):
    serializer_class = ComputadorSerializer
    queryset = Computador.objects.all()

class CoordenadorViewSet(viewsets.ModelViewSet):
    serializer_class = CoordenadorSerializer
    queryset = Coordenador.objects.all()

class AlunoViewSet(viewsets.ModelViewSet):
    serializer_class = AlunoSerializer
    queryset = Aluno.objects.all()

class ProjetoViewSet(viewsets.ModelViewSet):
    serializer_class = ProjetoSerializer
    queryset = Projeto.objects.all()

class ReservaViewSet(viewsets.ModelViewSet):
    serializer_class = ReservaSerializer
    queryset = Reserva.objects.all()