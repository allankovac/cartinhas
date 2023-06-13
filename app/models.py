from django.db import models

# Create your models here.
class Posicao(models.Model):
    nome_resumido=models.CharField(max_length=3, default=None)
    nome_completo=models.CharField(max_length=50)
    def __str__(self):
        return self.nome_completo

class Time(models.Model):
    nome_resumido=models.CharField(max_length=3, default=None)
    nome_completo=models.CharField(max_length=50)

    def __str__(self):
        return self.nome_completo

class Atleta(models.Model):
    nome=models.CharField(max_length=50)
    reserva=models.BooleanField(default=False)
    time=models.ForeignKey(Time, on_delete=models.CASCADE)
    posicao=models.ForeignKey(Posicao, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nome}-{self.time.nome_completo}'

class Etapa(models.Model):
    nome=models.CharField(max_length=50)
    data_inicio=models.DateField()
    data_fim = models.DateField()

    def __str__(self):
        return f'{self.nome}'
class Rodada(models.Model):
    nome=models.CharField(max_length=50)
    data_inicio=models.DateField()
    data_fim = models.DateField()
    etapa = models.ForeignKey(Etapa, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nome} - {self.data_inicio} - {self.data_fim}'

class Nota(models.Model):
    valor = models.FloatField(max_length=50)
    rodada = models.ForeignKey(Rodada, on_delete=models.CASCADE)
    atleta = models.ForeignKey(Atleta, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.valor} - {self.atleta}'

    def retornaNotas(self):
        return Nota.objects.all()