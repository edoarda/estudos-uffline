from django.conf.urls import url
from . import views

app_name = 'database'

urlpatterns = [
    url(r'^$', views.LogView.as_view(), name='log'),
	url(r'^index/$', views.IndexView.as_view(), name = 'index'),
	url(r'^materia(<materia_codigo>[A-Z0-9a-z]+)/$', views.MenuMateriaView.as_view(), name = menumateria'),
]
