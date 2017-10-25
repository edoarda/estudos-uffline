from django.db import models

def upload_to(instance, filename):
    return 'img/%s/%s' % (instance.user.user.id, filename)

class Grupo(models.Model):
    def __str__(self):
        return self.materia_key

    t_inicio = models.DateTimeField('data e horário de inicio')
    t_fim = models.DateTimeField('data e horário de fim')
    n_total = models.PositiveSmallIntegerField(default=5)
    n_atual = models.PositiveSmallIntegerField(default=1)
    local = models.CharField(max_length=200)
    materia_key = models.ForeignKey('Materia', on_delete=models.PROTECT)

class Materia(models.Model):
    class Meta:
        unique_together = ('codigo', 'turma', 'periodo_key')

    def __str__(self):
        return self.nome

    codigo = models.CharField(max_length=8, primary_key=True)
    nome = models.CharField(max_length=40, default='me dê um nome de verdade')
    turma = models.CharField(max_length=2)
    periodo_key = models.ForeignKey('Periodo', on_delete=models.PROTECT, default=20001)

class Periodo(models.Model):
    def __str__(self):
        return self.periodo_nome

    periodo_nome = models.CharField(max_length=6,default='2000.1')
    periodo = models.PositiveIntegerField(primary_key=True)

class Recurso(models.Model):
    def __str__(self):
        return self.nome

    nome = models.CharField(max_length=80)
    descricao = models.CharField(max_length=500)
    materia_key= models.ForeignKey('Materia', on_delete=models.PROTECT, default='AAA00000')

class Foto(models.Model):

    recurso_id = models.ForeignKey('Recurso', on_delete=models.PROTECT)
    foto = models.ImageField(upload_to=upload_to)

class URL(models.Model):
    def __str__(self):
        return self.url

    recurso_id = models.ForeignKey('Recurso', on_delete=models.PROTECT)
    url = models.URLField('')

class DataProva(models.Model):
    def __str__(self):
        return
    data = models.DateField('')
    prova = models.CharField(max_length=2)
    periodo_key = models.ForeignKey('Periodo', on_delete=models.PROTECT, default=20001)
    materia_key = models.ForeignKey('Materia', on_delete=models.PROTECT, default=20001)
    #turma = models.ForeignKey('Materia', on_delete=models.PROTECT, null=True, blank=True, default='A1', tofield='turma')
    turma = models.CharField(max_length=2) # adeus integridade linda do meu bd

#class Choice(models.Model):
#    question = models.ForeignKey(Question, on_delete=models.PROTECT)
#    choice_text = models.CharField(max_length=200)
#    votes = models.IntegerField(default=0)
