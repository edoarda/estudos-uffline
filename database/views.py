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

def choose(request, materia_codigo):
	choice = Materia.get_object_or_404(Materia, pk=materia_codigo)
	return HttpResponseRedirect(reverse('database:menumateria', args = (choice.codigo,)))
# Create your views here.
