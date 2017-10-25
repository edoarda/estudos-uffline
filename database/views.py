from .models import Materia
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

#def menumateria(request, materia_codigo):
#	choice = get_object_or_404(Materia, Materia.objects.filter(codigo=materia_codigo))
    #codigo = materia_codigo
#	return HttpResponseRedirect(reverse('database:menumateria', args = (choice.codigo,)))
# Create your views here.

def menumateria(request, materia_codigo):
    treco = Materia.objects.filter(codigo=materia_codigo)
    return render(request, 'database/menumateria.html', {'nome' : treco})
