from django.contrib import admin
from django.urls import path, include
from produccion import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('rest.urls')),
    #Agregar los paths a los views.modelos 
    path('registro/', views.registro, name='registro'),
    path('modificar/', views.modificar, name='modificar'),
    path('consulta/', views.consulta, name='consulta'),

    
]

