from django.contrib import admin
from django.urls import path
from . import views#asi se importa todo el archivo views para llamar a la clase visata vista basada en clase
urlpatterns = [
    path('prueba/', views.PruebaView.as_view()),
    path('lista/', views.PruebaListView.as_view()),
    path('lis/', views.ListaPrueba.as_view()),#asi se maneja las urls basadas en clases
    path('add/', views.PruebaCreateView.as_view(), name= 'prueba_add'),
    path('resumen-fundation/', views.ResumenFoundationView.as_view(), name= 'resumen'),
]
