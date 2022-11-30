from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ComputadorViewSet, CoordenadorViewSet, AlunoViewSet, ProjetoViewSet, ReservaViewSet

####
router = DefaultRouter()
router.register(r'computador', ComputadorViewSet)
router.register(r'coordenador', CoordenadorViewSet)
router.register(r'aluno', AlunoViewSet)
router.register(r'projeto', ProjetoViewSet)
router.register(r'reserva', ReservaViewSet)

urlpatterns = [
    path("", include(router.urls))
]