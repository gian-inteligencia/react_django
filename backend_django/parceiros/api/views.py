# CÓDIGO CORRETO para: backend_django/parceiros/api/views.py

from rest_framework import viewsets, status
from rest_framework.response import Response
from ..models import Parceiro
from .serializers import ParceiroSerializer
from .. import services as parceiros_embedded_service

class ParceiroViewSet(viewsets.ModelViewSet):
    """
    Esta única classe cria automaticamente as rotas para:
    - GET /api/v1/parceiros/ (Listar todos)
    - GET /api/v1/parceiros/{id}/ (Ver um)
    - POST /api/v1/parceiros/ (Criar novo)
    - PUT /api/v1/parceiros/{id}/ (Atualizar)
    - DELETE /api/v1/parceiros/{id}/ (Deletar)
    """
    queryset = Parceiro.objects.filter(status=True)
    serializer_class = ParceiroSerializer

    # --- AQUI ESTÁ A LÓGICA DE NEGÓCIOS ---
    # Nós "interceptamos" o método de criação (POST)
    
    def create(self, request, *args, **kwargs):
        # 1. Os dados do form (JSON) já vêm validados pelo serializer
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data # Dados prontos para usar
        
        email_para_api = data.get('email_gestor')
        
        try:
            # 2. Chama seu serviço (o mesmo código do Flask)
            # (Certifique-se que você copiou seu 'services/parceiros_embedded_service.py'
            # para 'parceiros/services.py' como eu instruí)
            api_id, erro_api = parceiros_embedded_service.criar_parceiro_completo(data)
            
            if erro_api:
                # Se a API externa falhar, retorna um erro 400
                return Response({"detail": erro_api}, status=status.HTTP_400_BAD_REQUEST)

            # 3. Salva no banco de dados local
            # Note que não usamos 'db.add_parceiro', o serializer faz isso
            parceiro = serializer.save(api_user_id=api_id)
            
            # Retorna o JSON do novo parceiro e um status 201 (Created)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except Exception as e:
            # 4. Rollback!
            parceiros_embedded_service.rollback_criacao_usuario(email_para_api)
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # (Você faria o mesmo 'override' para os métodos 'update' e 'destroy'
    #  para chamar 'atualizar_usuario' e 'deletar_usuario' da sua service)