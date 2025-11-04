# CÓDIGO para: backend_django/parceiros/admin.py

from django.contrib import admin
from .models import Parceiro # Importa o modelo que você criou

@admin.register(Parceiro)
class ParceiroAdmin(admin.ModelAdmin):
    # Mostra estes campos na lista
    list_display = ('nome_fantasia', 'email_gestor', 'tipo', 'status', 'senha_definida')
    # Adiciona filtros na lateral
    list_filter = ('tipo', 'status', 'senha_definida')
    # Adiciona uma barra de busca
    search_fields = ('nome_fantasia', 'email_gestor', 'cnpj')