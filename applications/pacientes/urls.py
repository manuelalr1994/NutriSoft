from django.contrib import admin
from django.urls import path, include

app_name = 'pacientes'

urlpatterns = [
    path('datos-generales/', include('applications.pacientes.datos_generales.urls', namespace='datos_generales')),
    path('', include('applications.pacientes.mediciones.urls', namespace='mediciones')),
]