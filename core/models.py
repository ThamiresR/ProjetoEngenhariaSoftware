from django.db import models
from django.db.models.fields.related import ForeignKey
# Create your models here.
class Computador(models.Model):
    id = models.AutoField(primary_key=True)
    descricao = models.TextField()

    def __str__(self):
        return self.descricao

class Coordenador(models.Model):
    name = models.CharField("Name", max_length=240)
    email = models.EmailField()
    login = models.CharField("Login", max_length=240)
    senha= models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Aluno(models.Model):
    name = models.CharField("Name", max_length=240)
    email = models.EmailField()
    login = models.CharField("Login", max_length=240)
    senha= models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Projeto(models.Model):
    titulo = models.CharField("Titulo", max_length=240)
    descricao = models.CharField("Descriccao", max_length=240)
    dataInicio = models.DateField()
    dataFim = models.DateField()
    coordenador = ForeignKey(Coordenador, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
   
class Reserva(models.Model):
    id_computador = ForeignKey(Computador, on_delete=models.CASCADE)
    id_aluno = ForeignKey(Aluno, on_delete=models.CASCADE)

    data = models.DateField()
    Horarios = (
        ("1", "08:00 ás 09:00"),
        ("2", "09:00 ás 10:00"),
        ("3", "10:00 ás 11:00"),
        ("4", "13:00 ás 14:00"),
        ("5", "14:00 ás 15:00"),
        ("6", "15:00 ás 16:00"),
        ("7", "16:00 ás 17:00"),
    )
    horario = models.CharField(max_length=10, choices=Horarios)

    class Meta:
        unique_together = ('horario', 'data')

    def __str__(self):
        return f'{self.data.strftime("%b %d %Y")} - {self.get_horario_display()} - {self.id_aluno}'