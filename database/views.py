from .models import Materia
from .models import Grupo
from .models import DataProva
from .models import Recurso

from django.http import HttpResponseRedirect
from django.views import generic
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

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
