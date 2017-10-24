from .models import Materia
from django.http import HttpResponseRedirect
from django.views import generic
from django.shortcuts import get_object_or_404, render

class LogView(generic.ListView):
	model = Materia
	template_name = 'database/log.html'

class IndexView(generic.ListView):
	model = Materia
	template_name = 'database/index.html'
def choose(request, codigo):
	choice = Materia.get(pk = request.GET['choice'])

# Create your views here.
