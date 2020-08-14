
from django.contrib import admin
from django.urls import path
from .import views
app_name= "persona_app"
urlpatterns = [

    path('', views.InicioView.as_view()),

    path('lista-todo-empleado/', views.ListaAllEmpleados.as_view(), name ='empleados'),
    path('lista-empleados-admin/', views.ListaAEmpleadosAdmin.as_view(), name= 'empleados_admin'),
   
    path('lista-by-area/<shorname>/', views.ListaByeAreEmpleados.as_view(), name='empleados_area'),
    path('BUSCAR-EMPLEADO/', views.LiaEmpleadosBykword.as_view()),
    path('listar-habilidaes/', views.ListaHabilidadesEmpleado.as_view()),
    path('ver-empleado/<pk>/', views.EmpleadoDetailView.as_view(), name='empleado_detail'),#el pk es para identificar de quein se queire ver la accio
    path('success', views.SuccessView.as_view(), name = 'correcto'),
    path('add-empleado/', views.EmpleadoCreateView.as_view(),name = 'empleado_add'),
    
    path('update-emple/<pk>/', views.EmpleadoUpdateView.as_view(), 
        name='modificar_empleado'),
 
    path('delete-empleado/<pk>/', views.EmpleadoDeleteView.as_view(), name = 'ELIMINAR-EMPLEADO'),

]


