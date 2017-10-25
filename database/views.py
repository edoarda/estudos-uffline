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
	all_models_dict = {
        "template_name": "contacts/index.html",
        "queryset": Individual.objects.all(),
        "extra_context" : {"grupo_list" : Grupo.objects.all(),
                           "dataprova_list": DataProva.objects.all(),
						   "material_list": Material.object.all(),
                           #and so on for all the desired models...
                           }
    }

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
