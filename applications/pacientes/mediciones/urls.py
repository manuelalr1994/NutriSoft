from unicodedata import name
from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'mediciones'

# Establecemos las URL de esta view
urlpatterns = [
    #path('registrar/', RegistrarEmpresas.as_view(), name='registro'),
    #path('nomina/catalogos/empresas/lista', ListaEmpresas.as_view(), name='lista_empresas'),
    #path('nomina/catalogos/empresas/actualizar/<int:pk>', ActualizarEmpresas.as_view(), name='actualizar_empresas'),
    #path('nomina/catalogos/empresas/consultar/<int:pk>', ConsultarEmpresas.as_view(), name='consultar_empresas'),
]