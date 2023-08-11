from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('miembros/', views.members, name='members'),
    path('miembros/details/<int:id>', views.details, name='details'),
    path('addrecord/', views.addrecord, name='addrecord'),
    path('success/', views.success, name='success'),
    path('socios/', views.allsocios, name='allsocios'),
    path('socios/editar/<int:id>', views.editar, name='editar'),
    path('socios/addsocio/', views.addsocio, name='addsocio'),
    path('socios/addsocio/guardarsocio/', views.guardarsocio, name='guardarsocio'),
    path('exito/', views.exito, name='exito'),
    path('registro/afiliar/', views.afiliar, name='afiliar'),
    path('registro/identificacion/', views.identificacion, name='identificacion'),
    path('registro/identificacion/acceso/', views.acceso, name='acceso'),    #/registro/identificacion/acceso/
    path('registro/inscripcion/', views.inscripcion, name='inscripcion'),
    path('registro/socio/', views.socio, name='socio'),
    path('registro/socio/guardar/', views.guardar, name='guardar'),
    path('registro/usuario/', views.usuario, name='usuario'),
    path('testing/', views.testing, name='testing'),
]