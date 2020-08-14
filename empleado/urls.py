
from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings#importa configuracion de django
from django.conf.urls.static import static#genera urls staticas

urlpatterns = [

    path('admin/', admin.site.urls),
    #incluimod las apps de departamento desde aqui las activamos
    re_path('', include('aplications.departamento.urls')),
    re_path('', include('aplications.persona.urls')),
    re_path('', include('aplications.home.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)#con esto crea una url para poder ver imaenes en el navegador
