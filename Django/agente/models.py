# Título: Agente
# Descrição: Classe agente
# Autor: Walysson dos Reis
# Criação: 12/05/2021
# Atualização: 12/05/2021

# coding: utf-8

from django.db import models
from categoria.models import Categoria

class Agente(models.Model):
    nome=models.CharField(max_length=255)
    cpf_cnpj=models.CharField(max_length=255)
    categoria=models.ManyToManyField(Categoria)
    telefone=models.CharField(max_length=255)
    endereco=models.CharField(max_length=255)
    descricao=models.TextField()
    odt_info=models.TextField()

    def cadAgente(self):
        pass