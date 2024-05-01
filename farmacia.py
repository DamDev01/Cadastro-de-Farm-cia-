from model.associado import Associado
from model.colaborador import Colaborador
from model.fornecedor import Fornecedor

class Pessoa:
    def __init__(self, nome, endereco, telefone):
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone

class Farmacia(Pessoa):
    def __init__(self, nome, endereco, telefone, numero_associado):
        super().__init__(nome, endereco, telefone)
        self.numero_associado = numero_associado
