from .models import Materia
from .models import Grupo
from .models import DataProva
from .models import Recurso

from django.http import HttpResponseRedirect
from django.views import generic
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.forms import modelformset_factory

class LogView(generic.ListView):
	model = Materia
	template_name = 'database/log.html'

class IndexView(generic.ListView):
	model = Materia
	template_name = 'database/index.html'

class MenuMateriaView(generic.ListView):
	model = Materia
	template_name = 'database/menumateria.html'
	def get_context_data(self, **kwargs):
		context = super(MenuMateriaView, self).get_context_data(**kwargs)
		context['nome_disc'] = Materia.objects.filter(codigo=self.kwargs['materia_codigo'])
		context['grupo_list'] = Grupo.objects.filter(materia_key=self.kwargs['materia_codigo'])
		context['dataprova_list'] = DataProva.objects.filter(materia_key=self.kwargs['materia_codigo'])
		context['recurso_list'] = Recurso.objects.filter(materia_key=self.kwargs['materia_codigo'])
		return context

#def menumateria(request, materia_codigo):
#	choice = get_object_or_404(Materia, Materia.objects.filter(codigo=materia_codigo))
    #codigo = materia_codigo
#	return HttpResponseRedirect(reverse('database:menumateria', args = (choice.codigo,)))
# Create your views here.

def menumateria(request, materia_codigo):
    #treco = Grupo.objects.filter(materia_key = materia_codigo)
    #treco = treco.order_by(+t_fim)
    treco = Materia.objects.filter(codigo=materia_codigo)
    return render(request, 'database/menumateria.html', {'nome' : treco})

class AddGrupoView(generic.ListView):
	model = Materia
	template_name = 'database/addgrupo.html'

def AddGrupoView(request):
	GrupoFormSet = modelformset_factory(Grupo, fields=('__all__'))
	if request.method == 'POST':
		formset = GrupoFormSet(request.POST, request.FILES)
		if formset.is_valid():
			formset.save()
	else: 
		formset = GrupoFormSet()
	return render(request, 'addgrupo.html', {'formset':formset})

class AddDataView(generic.ListView):
	model = Materia
	template_name = 'database/addgrupo.html'

def AddDataView(request):
	DataFormSet = modelformset_factory(DataProva, fields=('__all__'))
	if request.method == 'POST':
		formset = DataFormSet(request.POST, request.FILES)
		if formset.is_valid():
			formset.save()
	else: 
		formset = DataFormSet()
	return render(request, 'addgrupo.html', {'formset':formset})


