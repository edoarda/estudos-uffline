from django.db import models

class Grupo(models.Model):
    t_inicio = models.DateTimeField('data e horário de inicio')
    t_fim = models.DateTimeField('data e horário de fim')
    n_total = models.PositiveSmallIntegerField(default=5)
    n_atual = models.PositiveSmallIntegerField(default=1)
    local = models.Charfield(max_length=200)
    materia = models.ForeignKey('Materia', on_delete=models.RESTRICT)

class Materia(models.Model):
    class Meta:
        unique_together = ('codigo', 'turma')
    codigo = models.Charfield(max_length=8, primary_key=True)
    turma = models.Charfield(max_length=2)
    periodo = models.ForeignKey('Periodo', on_delete=models.RESTRICT)

class Periodo(models.Model):
    materia = models.ForeignKey('Materia', on_delete=models.RESTRICT)
    periodo = models.PositiveSmallIntegerField(primary_key=True)

class Recursos(model.Model):
    nome = models.Charfield(max_length=80)
    descricao = models.CharField(max_length=500)

class Fotos(model.Model):
    recurso_id = models.ForeignKey('Recursos', on_delete=models.CASCADE)
    foto = models.ImageField(upload_to=recurso_id + '/')

class URLs(model.Models):
    recurso_id = models.ForeignKey('Recursos', on_delete=models.CASCADE)
    url = models.UrlField('')

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
