from django.conf.urls import url
from . import views

app_name = 'database'

urlpatterns = [
    url(r'^$', views.LogView.as_view(), name='log'),
	url(r'^addgrupo.html', views.AddGrupoView, name = 'addgrupo'),
	url(r'^adddata.html', views.AddDataView, name = 'adddata'),
	url(r'^index/$', views.IndexView.as_view(), name = 'index'),
	url(r'^materia(?P<materia_codigo>[A-Z0-9a-z]+)/menumateria.html$', views.MenuMateriaView.as_view(), name = 'menumateria'),
]
