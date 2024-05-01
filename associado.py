from .pessoa import Pessoa


class Associado(Pessoa):
    def __init__(self, id, nome, logradouro, numero, cep, bairro, cidade, uf, telefone, cpf_cnpj, situacao, numero_associado=None):
        super().__init__(id, nome, logradouro, numero, cep, bairro, cidade, uf, telefone, cpf_cnpj)
        self.situacao = situacao
        self.numero_associado = numero_associado