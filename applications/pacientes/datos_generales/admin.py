from django.contrib import admin
from .models import Pacientes
# Register your models here.

# usu: mleon
# email: manuel.alr1994@gmail.com
# pass: flaskdjango123

admin.site.register(Pacientes)

class PacientesAdmin(admin.ModelAdmin):
    list_display = (
        'codigo',
        'nombre',
        'email',
    )

    search_fields = ('nombre','codigo')
    list_filter = ('sexo')

    filter_horizontal = ('sexo')

admin.site.register(Pacientes, PacientesAdmin)