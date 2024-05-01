from .pessoa import Pessoa

class Colaborador(Pessoa):
    
    def __init__(self, id, nome, logradouro, numero, cep, bairro, cidade, uf, telefone, cpf_cnpj, cargo=None):
        super().__init__(id, nome, logradouro, numero, cep, bairro, cidade, uf, telefone, cpf_cnpj)
        self.cargo = cargo