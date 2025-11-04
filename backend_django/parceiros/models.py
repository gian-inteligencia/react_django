# CÓDIGO CORRETO para: backend_django/parceiros/models.py

from django.db import models

# Esta é a definição do modelo (tabela) que o Django entende.
# É o equivalente ao seu antigo `parceiro_db.py`, mas no formato ORM.

class Parceiro(models.Model):
    # O ID (PK) é automático no Django
    api_user_id = models.CharField(max_length=50, null=True, blank=True, unique=True)
    nome_ajustado = models.CharField(max_length=255)
    
    TIPO_CHOICES = [
        ('INDUSTRIA', 'Industria'),
        ('DISTRIBUIDOR', 'Distribuidor'),
    ]
    tipo = models.CharField(max_length=100, choices=TIPO_CHOICES)
    
    cnpj = models.CharField(max_length=20)
    nome_fantasia = models.CharField(max_length=255)
    razao_social = models.CharField(max_length=255)
    gestor = models.CharField(max_length=255)
    telefone_gestor = models.CharField(max_length=20)
    email_gestor = models.EmailField(max_length=255, unique=True)
    
    data_entrada = models.DateField()
    data_saida = models.DateField(null=True, blank=True)
    
    status = models.BooleanField(default=True)
    senha_definida = models.BooleanField(default=False)
    
    # O Django gerencia data_atualizacao automaticamente
    data_atualizacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome_fantasia