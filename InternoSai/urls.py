from django.urls import path, include
from .views import home
from rest_framework import routers
from . import views
from InternoSai.views import RegistroFacturaElectronica, RegistroMensajeria, AdministraRecursos


urlpatterns = [
    path('home', home, name='home'),
    path('RegistroFacturaElectronica', RegistroFacturaElectronica.as_view(), name='Reg_Fac_Electronica'),
    path('RegistroMensajeria', RegistroMensajeria.as_view(), name='Reg_Mensajeria'),
    path('AdministraRecursos', AdministraRecursos.as_view(), name='Administra_Recursos'),
]
 