from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductoViewSet, PlantaViewSet, RegistroProduccionViewSet

router = DefaultRouter()
router.register(r'productos', ProductoViewSet)
router.register(r'plantas', PlantaViewSet)
router.register(r'registros', RegistroProduccionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]