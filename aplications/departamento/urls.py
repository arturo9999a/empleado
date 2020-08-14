
from django.contrib import admin
from django.urls import path
from . import views

app_name = "departamento_app"

def departamen(self):
    print('____________prueba_____________')


urlpatterns = [
    path('departament/', departamen),
    path('nwe-departamento/', views.NewDepartamentoView.as_view(), name= 'nuevo_departamento'),
    path('departamento-lista/', views.DepartmanetoListView.as_view(), name= 'departamento-list'),
]
