from django.db import models


class Grupo(models.Model):
    t_inicio = models.DateTimeField('data e horário de inicio')
    t_fim = models.DateTimeField('data e horário de fim')
    n_total = models.PositiveSmallIntegerField(default=5)
    n_atual = models.PositiveSmallIntegerField(default=1)
    local = models.Charfield(max_length=200)

class Materia(models.Model):
    class Meta:
        unique_together = ('codigo', 'turma')
    codigo = models.Charfield(max_length=8, primary_key=True)
    turma = models.Charfield(max_length=2)
    periodo = models.ForeignKey('Periodo', on_delete=models.CASCADE)

class Periodo(models.Model):
    periodo = models.PositiveSmallIntegerField()

class Recursos(model.Model):

    
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
