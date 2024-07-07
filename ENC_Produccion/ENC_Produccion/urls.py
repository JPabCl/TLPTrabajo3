from django.contrib import admin
from django.urls import path, include
from produccion import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('rest.urls')),
    #Agregar los paths a los views.modelos 
    path('', views.inicio, name="home"),
    path('registro/', views.registro, name='registro'),
    path('modificar/', views.modificar, name='modificar'),
    path('consulta/', views.consulta, name='consulta'),
    path('login/', views.login_view, name='login'),
    path('crear_usuario/', views.crear_usuario_view, name='crear_usuario'),
    path('logout/', views.logout_view, name='logout'),
        
]

