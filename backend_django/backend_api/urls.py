from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from parceiros.api.views import ParceiroViewSet # Importa nossa View da API

# Configura o roteador do DRF
router = DefaultRouter()
router.register(r'parceiros', ParceiroViewSet, basename='parceiro')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)), # Aqui está a rota da nossa API
]