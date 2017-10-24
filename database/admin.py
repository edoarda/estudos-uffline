from django.contrib import admin

from .models import Grupo
from .models import Materia
from .models import Periodo
from .models import Recurso
from .models import Foto
from .models import URL

admin.site.register(Grupo)
admin.site.register(Materia)
admin.site.register(Periodo)
admin.site.register(Recurso)
admin.site.register(Foto)
admin.site.register(URL)
