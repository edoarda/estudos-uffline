from django.conf.urls import url

from . import views

app_name = 'database'
urlpatterns = [
    url(r'^$', views.LogView.as_view(), name='log'),
	url(r'^index/$', views.IndexView.as_view(), name = 'index'),
]
