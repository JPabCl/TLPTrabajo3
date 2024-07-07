from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name='index'),
   path('registrar/', views.registrar_produccion, name='registrar_produccion'),
   path('lista/', views.lista_produccion, name='lista_produccion'),
]
