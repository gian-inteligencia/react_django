# CÓDIGO para: backend_django/parceiros/api/serializers.py

from rest_framework import serializers
from ..models import Parceiro  # (..models sobe um nível para /parceiros/models.py)

class ParceiroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parceiro
        # Simplesmente listamos os campos que a API deve expor
        fields = [
            'id', 'api_user_id', 'nome_ajustado', 'tipo', 'cnpj', 
            'nome_fantasia', 'razao_social', 'gestor', 'telefone_gestor', 
            'email_gestor', 'data_entrada', 'data_saida', 'senha_definida'
        ]
        # O email_gestor não pode ser editado após a criação
        read_only_fields = ['email_gestor']