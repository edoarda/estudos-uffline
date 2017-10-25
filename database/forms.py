from django import forms

class AddGrupo(forms.Form):
	date = forms.DateField(default='2018-5-1')
    t_inicio = forms.TimeField(default='09:00')
    t_fim = forms.TimeField(default='22:00')
    n_total = forms.PositiveSmallIntegerField(default=5)
    n_atual = forms.PositiveSmallIntegerField(default=1)
    local = forms.CharField(max_length=200)
